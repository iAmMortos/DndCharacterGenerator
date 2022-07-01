
from model.pc.player_character import PlayerCharacter
from utils.data_file_loader import DataFileLoader as DFL


xml = DFL().load_compendium_xml('characters/Melodias')
mel = PlayerCharacter(xml)

print(mel.character.name)
