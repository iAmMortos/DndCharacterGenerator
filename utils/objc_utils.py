
from objc_util import *


@on_main_thread
def print_html(input, orientation='P'):
  '''takes HTML input and formats it for printing. Uses the built in ios UI print dialogue. Orientation should be 'P' or 'L' '''
  html = ObjCClass('UIMarkupTextPrintFormatter').alloc().initWithMarkupText_(ns(input))
  printController = ObjCClass('UIPrintInteractionController').sharedPrintController()
  printInfo = ObjCClass('UIPrintInfo').printInfoWithDictionary_(None)
  printInfo.orientation = int(orientation.upper() == 'L')
  printController.printInfo = printInfo
  printController.setPrintFormatter_(html)
  printController.presentAnimated_completionHandler_(0, None)
  
