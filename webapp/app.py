from website import create_app
import os
app = create_app()

if __name__ == '__main__':
    extra_dirs = [
        r'C:\Users\Christo\Documents\Remote\ChristoPC\College\ANU\2024_Semester_2\HackANU\TheBackstreetBoys\webapp\website\templates',
    ]
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = os.path.join(dirname, filename)
                if os.path.isfile(filename):
                    extra_files.append(filename)
    app.run(threaded=True, extra_files=extra_files)
