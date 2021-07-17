# Sources
#  - http://www.sunshine2k.de/articles/coding/crc/understanding_crc.html#ch5
#  - https://forums.pcsx2.net/Thread-Celsius-FFX-2-Save-game-editor?pid=182634#pid182634
#  - https://gamefaqs.gamespot.com/boards/197344-final-fantasy-x/48762606
from enum import Enum


class Game(Enum):
     FFX = 1
     FFX2 = 2


# from https://forums.pcsx2.net/Thread-Celsius-FFX-2-Save-game-editor?pid=182634#pid182634
CRC_START_OFFSET = 0x40
CRC_SEED = 0xFFFF

CRC_END_FFX = 0x64F8  # 25848 bytes - the size of FFX International Edition save
CRC_END_FFX2 = 0x16270  # 90736 bytes - the size of FFX-2 save

# Allegedly there are two checksum locations according to https://gamefaqs.gamespot.com/boards/197344-final-fantasy-x/48762606
CHECKSUM_LOCATION_A = 0x1A  # Shared with FFX and FFX2
CHECKSUM_LOCATION_FFX_B = 0x64F4
CHECKSUM_LOCATION_FFX2_B = 0x16268


def _maskTo8Bits(number):
  return number & 0xFF


def _maskTo16Bits(number):
  return number & 0xFFFF


def _generate_FFX_CRC16_table():
  """Creates the CRC16 table used by FFX. It's roughly CRC-16-CCITT

  Implementation based heavily off of
  http://www.sunshine2k.de/articles/coding/crc/understanding_crc.html#ch5

  Returns:
    Returns a table of length 256 containing the CRC16 lookup values for FFX.
  """
  generator = 0x1021  # CRC-16-CCITT values
  crc16_table = [None] * 256

  # iterate over all possible input byte values 0 - 255.
  for dividend in range(len(crc16_table)):
    # move dividend byte into MSB of 16Bit CRC
    current_byte = _maskTo16Bits(dividend << 8)

    for bit in range(8):  # Iterate all 8 bits
      if (current_byte & 0x8000) != 0:
        current_byte = current_byte << 1
        current_byte = current_byte ^ generator
      else:
        current_byte = current_byte << 1
      current_byte = _maskTo16Bits(current_byte)

    crc16_table[dividend] = current_byte

  # According to https://forums.pcsx2.net/Thread-Celsius-FFX-2-Save-game-editor?pid=182634#pid182634
  # there is a bug in the CRC16 table generation used by the FFX save algorithm.
  # To remedy this, set the final byte to 0x0.
  crc16_table[len(crc16_table) - 1] = 0x0

  return crc16_table


def _compute_checksum(save_file_bytes, game):
  """
  Computes the FFX checksum.

  Implementation based heavily off of
  https://forums.pcsx2.net/Thread-Celsius-FFX-2-Save-game-editor?pid=182634#pid182634

  Also referenced:
  http://www.sunshine2k.de/articles/coding/crc/understanding_crc.html#ch5

  Returns:
    Two 8-bit values. The first is the lower byte, the second is the upper byte.
  """
  crc16_table = _generate_FFX_CRC16_table()
  checksum = CRC_SEED
  crc_end = CRC_END_FFX if game is Game.FFX else CRC_END_FFX2
  for byte_index in range(CRC_START_OFFSET, crc_end):
    checksum_location = CHECKSUM_LOCATION_FFX_B if game is Game.FFX else CHECKSUM_LOCATION_FFX2_B
    # Ignore the existing checksum value, if one is present. Treat it as `0`.
    if (byte_index == checksum_location or byte_index == checksum_location + 1):
      table_index = _maskTo8Bits((checksum >> 8) ^ 0)
    else:
      # XOR-in next input byte into MSB of checksum, that's the new intermediate dividend.
      table_index = _maskTo8Bits((checksum >> 8) ^ save_file_bytes[byte_index])
    # Shift out the MSB used for division per lookuptable and XOR with the remainder.
    checksum = (checksum << 8) ^ crc16_table[table_index]
  checksum = checksum ^ CRC_SEED

  checksum_lower_byte = _maskTo8Bits(checksum)
  checksum_upper_byte = _maskTo8Bits(checksum >> 8)
  return checksum_lower_byte, checksum_upper_byte


def compute_FFX2_checksum(save_file_bytes):
  return _compute_checksum(save_file_bytes, Game.FFX2)


def compute_FFX_checksum(save_file_bytes):
  return _compute_checksum(save_file_bytes, Game.FFX)