import aspose.slides as slides

# load presentation
with slides.Presentation("../input/title.pptx") as presentation:
    # select paragraph to add effect
    autoShape = presentation.slides[0].shapes[0]
    paragraph = autoShape.text_frame.paragraphs[0]

    # add Fly animation effect to selected paragraph
    effect = presentation.slides[0].timeline.main_sequence.add_effect(paragraph, slides.animation.EffectType.FLY, slides.animation.EffectSubtype.RIGHT, slides.animation.EffectTriggerType.ON_CLICK)
    autoShape = presentation.slides[0].shapes[1]
    paragraph = autoShape.text_frame.paragraphs[0]

    # add Fly animation effect to selected paragraph
    effect = presentation.slides[0].timeline.main_sequence.add_effect(paragraph, slides.animation.EffectType.FLY, slides.animation.EffectSubtype.LEFT, slides.animation.EffectTriggerType.ON_CLICK)
    

    # save presentation
    presentation.save("AnimationEffectinParagraph.pptx", slides.export.SaveFormat.PPTX)
    
# # load presentation
# with slides.Presentation("presentation.pptx") as presentation:
#     # select paragraph to add effect
#     autoShape = presentation.slides[0].shapes[0]
#     paragraph = autoShape.text_frame.paragraphs[0]

#     # add Fly animation effect to selected paragraph
#     effect = presentation.slides[0].timeline.main_sequence.add_effect(paragraph, slides.animation.EffectType.FLY, slides.animation.EffectSubtype.LEFT, slides.animation.EffectTriggerType.ON_CLICK)

#     # save presentation
#     presentation.save("AnimationEffectinParagraph.pptx", slides.export.SaveFormat.PPTX)    