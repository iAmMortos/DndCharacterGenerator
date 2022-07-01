
from views.dpr_tool_view import DPRToolView

if __name__ == '__main__':
  dprv = DPRToolView.load_view()
  dprv.present(style='fullscreen', hide_title_bar=False, orientations=['portrait'])
