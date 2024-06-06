# The following code does not work
# 
# 
# The following code does not work
import win32com.client

# Open an existing PowerPoint presentation
ppt_app = win32com.client.Dispatch("PowerPoint.Application")
presentation = ppt_app.Presentations.Open("../input/title.pptx")

# Get a slide by index (0-based)
slide = presentation.Slides(0)

# Add a rectangle shape to the slide
left = 100
top = 100
width = 200
height = 100
shape = slide.Shapes.AddShape(1, left, top, width, height)  # 1 represents a rectangle shape

# Add an entrance animation to the shape
effect = shape.AnimationSettings.AddEffect(EffectType=1)  # 1 represents an entrance animation
effect.Timing.Duration = 2  # Animation duration in seconds

# Save the modified presentation
presentation.SaveAs("../output/animations.pptx")

# Close the PowerPoint application
ppt_app.Quit()
