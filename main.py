import AppKit
import Quartz
import os
from PIL import Image

from ocr import do_ocr


# Define the window class
class MyWindow(AppKit.NSWindow):
    def init(self):
        # Get size of screen
        screenSize = AppKit.NSScreen.mainScreen().frame()
        width, height = (int(screenSize.size.width), int(screenSize.size.height))
        print(width, height)

        contentRect = AppKit.NSMakeRect(0, 0, width, height)
        styleMask = (
            AppKit.NSWindowStyleMaskTitled |
            AppKit.NSWindowStyleMaskClosable |
            AppKit.NSWindowStyleMaskMiniaturizable |
            AppKit.NSWindowStyleMaskResizable
            # AppKit.NSWindowStyleMaskFullScreen
        )
        backing = AppKit.NSBackingStoreBuffered
        self = super(MyWindow, self).init()
        if self is not None:
            self = self.alloc().initWithContentRect_styleMask_backing_defer_(
                contentRect, styleMask, backing, False
            )
            self.setTitle_("My Window")
            self.setAlphaValue_(0.5)
            self.setLevel_(AppKit.NSFloatingWindowLevel)

            # Create a text field
            # textField = AppKit.NSTextField.alloc().initWithFrame_(
            #     AppKit.NSMakeRect(70, 500, 200, 10)
            # )
            # textField.setStringValue_("Hello, World!")
            # textField.setBezeled_(False)
            # textField.setDrawsBackground_(False)
            
            # Add the text field to the window
            # self.contentView().addSubview_(textField)

            self.ocrTimer = AppKit.NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
                3.0, self, "performOCR:", None, True
            )

        return self
    
    # Override ignoresMouseEvents to make window click-through
    def ignoresMouseEvents(self):
        return True

    def performOCR_(self, userInfo):
        print("a")
        
        # Stage
        # Define the region of interest within the screen frame
        region = Quartz.CGRectMake(700, 0, 300, 50)
        
        # Create a bitmap image of the region
        image = Quartz.CGDisplayCreateImageForRect(
            Quartz.CGMainDisplayID(), region
        )
                
        # Create a PIL image from the bitmap data
        width, height = Quartz.CGImageGetWidth(image), Quartz.CGImageGetHeight(image)
        bytesPerRow = Quartz.CGImageGetBytesPerRow(image)
        rawData = Quartz.CGDataProviderCopyData(Quartz.CGImageGetDataProvider(image))
        pilImage = Image.frombytes("RGB", (width, height), rawData, "raw", "BGRX", bytesPerRow)

        # time_stamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        pilImage.save("./captured_images/stage.png")
        res = do_ocr("./captured_images/stage.png")
        print(res)

        # ocr_result = pytesseract.image_to_string(pilImage)
        # print("stage:", ocr_result)

        # Traits
        # Define the region of interest within the screen frame
        region = Quartz.CGRectMake(0, 285, 200, 40)
        
        # Create a bitmap image of the region
        image = Quartz.CGDisplayCreateImageForRect(
            Quartz.CGMainDisplayID(), region
        )
                
        # Create a PIL image from the bitmap data
        width, height = Quartz.CGImageGetWidth(image), Quartz.CGImageGetHeight(image)
        bytesPerRow = Quartz.CGImageGetBytesPerRow(image)
        rawData = Quartz.CGDataProviderCopyData(Quartz.CGImageGetDataProvider(image))
        pilImage = Image.frombytes("RGB", (width, height), rawData, "raw", "BGRX", bytesPerRow)

        # time_stamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        pilImage.save("./captured_images/trait1.png")

        # ocr_result = pytesseract.image_to_string(pilImage, lang="chi_tra")
        # print("trait1:", ocr_result)

        # Players
        # Define the region of interest within the screen frame
        region = Quartz.CGRectMake(1700, 180, 200, 600)
        
        # Create a bitmap image of the region
        image = Quartz.CGDisplayCreateImageForRect(
            Quartz.CGMainDisplayID(), region
        )
                
        # Create a PIL image from the bitmap data
        width, height = Quartz.CGImageGetWidth(image), Quartz.CGImageGetHeight(image)
        bytesPerRow = Quartz.CGImageGetBytesPerRow(image)
        rawData = Quartz.CGDataProviderCopyData(Quartz.CGImageGetDataProvider(image))
        pilImage = Image.frombytes("RGB", (width, height), rawData, "raw", "BGRX", bytesPerRow)

        # time_stamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        pilImage.save("./captured_images/player1.png")

        # ocr_result = pytesseract.image_to_string(pilImage)
        # print("player1:", ocr_result)


if not os.path.exists("./captured_images"):
    os.makedirs("./captured_images")

# Create the window
myWindow = MyWindow.alloc().init()

# Set window level to floating window
myWindow.setLevel_(AppKit.NSFloatingWindowLevel)

# Display the window
myWindow.makeKeyAndOrderFront_(None)

# Run the app event loop
AppKit.NSApplication.sharedApplication().run()
