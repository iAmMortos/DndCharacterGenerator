
import io

def gen_spell_block(spell):
  with io.open('views/markdown/templates/spell.md') as f:
    block = f.read()
  block = block.replace('{name}', spell.name)
  block = block.replace('{spell-details}', spell.slr_txt)
  block = block.replace('{cast-time}', str(spell.time))
  block = block.replace('{range}', str(spell.range))
  block = block.replace('{components}', str(spell.components))
  block = block.replace('{concentration}', '')
  block = block.replace('{duration}', str(spell.duration))
  block = block.replace('{body}', spell.text)
  return block
