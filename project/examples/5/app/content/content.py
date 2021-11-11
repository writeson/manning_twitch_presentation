from flask import render_template
from . import content_bp

@content_bp.get("/content")
def content():
    content = [ 
        {
            "title": "Content Item 1",
            "image_filename": "puppy_1.jpg",
            "text": [
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Turpis tincidunt id aliquet risus feugiat in ante metus. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc. Neque vitae tempus quam pellentesque nec nam aliquam sem et. Urna duis convallis convallis tellus id interdum velit laoreet id. Magna fringilla urna porttitor rhoncus dolor purus. Sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra. Blandit massa enim nec dui nunc mattis enim. Sed enim ut sem viverra aliquet eget sit amet tellus. At erat pellentesque adipiscing commodo elit at imperdiet dui accumsan. Non curabitur gravida arcu ac tortor dignissim convallis.",
                "Ut enim blandit volutpat maecenas volutpat blandit aliquam etiam. Turpis egestas pretium aenean pharetra magna ac. Habitasse platea dictumst quisque sagittis purus sit. Laoreet sit amet cursus sit amet dictum. Tellus integer feugiat scelerisque varius morbi enim nunc faucibus a. Non diam phasellus vestibulum lorem sed. Iaculis urna id volutpat lacus laoreet. Interdum posuere lorem ipsum dolor sit. Et malesuada fames ac turpis egestas integer eget aliquet nibh. Integer feugiat scelerisque varius morbi enim nunc faucibus. Euismod nisi porta lorem mollis. Ornare suspendisse sed nisi lacus. Sed velit dignissim sodales ut eu sem integer vitae. Varius sit amet mattis vulputate enim nulla aliquet porttitor. Sed pulvinar proin gravida hendrerit lectus a."
            ]
        },
        {
            "title": "Content Item 2",
            "image_filename": "puppy_2.jpg",
            "text": [
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Turpis tincidunt id aliquet risus feugiat in ante metus. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc. Neque vitae tempus quam pellentesque nec nam aliquam sem et. Urna duis convallis convallis tellus id interdum velit laoreet id. Magna fringilla urna porttitor rhoncus dolor purus. Sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra. Blandit massa enim nec dui nunc mattis enim. Sed enim ut sem viverra aliquet eget sit amet tellus. At erat pellentesque adipiscing commodo elit at imperdiet dui accumsan. Non curabitur gravida arcu ac tortor dignissim convallis.",
                "Ut enim blandit volutpat maecenas volutpat blandit aliquam etiam. Turpis egestas pretium aenean pharetra magna ac. Habitasse platea dictumst quisque sagittis purus sit. Laoreet sit amet cursus sit amet dictum. Tellus integer feugiat scelerisque varius morbi enim nunc faucibus a. Non diam phasellus vestibulum lorem sed. Iaculis urna id volutpat lacus laoreet. Interdum posuere lorem ipsum dolor sit. Et malesuada fames ac turpis egestas integer eget aliquet nibh. Integer feugiat scelerisque varius morbi enim nunc faucibus. Euismod nisi porta lorem mollis. Ornare suspendisse sed nisi lacus. Sed velit dignissim sodales ut eu sem integer vitae. Varius sit amet mattis vulputate enim nulla aliquet porttitor. Sed pulvinar proin gravida hendrerit lectus a."
            ]
        },
        {
            "title": "Content Item 3",
            "image_filename": "puppy_3.jpg",
            "text": [
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Turpis tincidunt id aliquet risus feugiat in ante metus. Sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc. Neque vitae tempus quam pellentesque nec nam aliquam sem et. Urna duis convallis convallis tellus id interdum velit laoreet id. Magna fringilla urna porttitor rhoncus dolor purus. Sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra. Blandit massa enim nec dui nunc mattis enim. Sed enim ut sem viverra aliquet eget sit amet tellus. At erat pellentesque adipiscing commodo elit at imperdiet dui accumsan. Non curabitur gravida arcu ac tortor dignissim convallis.",
                "Ut enim blandit volutpat maecenas volutpat blandit aliquam etiam. Turpis egestas pretium aenean pharetra magna ac. Habitasse platea dictumst quisque sagittis purus sit. Laoreet sit amet cursus sit amet dictum. Tellus integer feugiat scelerisque varius morbi enim nunc faucibus a. Non diam phasellus vestibulum lorem sed. Iaculis urna id volutpat lacus laoreet. Interdum posuere lorem ipsum dolor sit. Et malesuada fames ac turpis egestas integer eget aliquet nibh. Integer feugiat scelerisque varius morbi enim nunc faucibus. Euismod nisi porta lorem mollis. Ornare suspendisse sed nisi lacus. Sed velit dignissim sodales ut eu sem integer vitae. Varius sit amet mattis vulputate enim nulla aliquet porttitor. Sed pulvinar proin gravida hendrerit lectus a."
            ]
        }
    ]
    return render_template("content.html", content=content)
