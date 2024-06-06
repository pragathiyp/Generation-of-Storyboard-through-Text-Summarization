# Path to your macro-enabled PowerPoint file
$presentationPath = "./AnimationEffectinParagraph.pptm"

# Create a PowerPoint application object
$pptApp = New-Object -ComObject PowerPoint.Application

# Set the application to be visible (for troubleshooting purposes)
$pptApp.Visible = $true

# Open the presentation
$presentation = $pptApp.Presentations.Open($presentationPath)

# Allow editing of the presentation
$presentation.ReadOnly = $false

# Run the macro
$macros = $presentation.VBProject.VBComponents
$macros.Item("Module1").CodeModule.AddFromString("Sub Auto_Open()" + "`r`n" + "AddBounceAnimationToTextBox" + "`r`n" + "End Sub")
$presentation.Application.Run("Auto_Open")

# Save and close the presentation
$presentation.Save()
$presentation.Close()

# Close the PowerPoint application
$pptApp.Quit()