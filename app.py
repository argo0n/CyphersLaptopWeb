from flask import Flask, redirect, render_template, request, abort
import os

app = Flask(__name__)

@app.route('/video')
def video():
    video_url = request.args.get('url')
    if video_url:
        # Parse the video name and file format
        video_name, file_format = os.path.splitext(os.path.basename(video_url))
        # Set the title and description
        title = video_name
        description = file_format
        # If the name or format could not be parsed, use a fallback value
        if not title:
            title = "Video"
        if not description:
            description = "Video file"
        return render_template('video.html', video_url=video_url, title=title, description=description)
    else:
        abort(400, "Missing url parameter")


if __name__ == '__main__':
    app.run()
