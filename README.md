# Readme.md

This repository contains the Python script to generate [my homepage](https://atakan-topaloglu.github.io/).

The overall design and initial script structure are built upon the excellent template provided by [Michael Niemeyer](https://m-niemeyer.github.io/). This setup is designed to be easy to adapt and maintain, as publications and projects are automatically crawled from BibTeX files.

## Atakan Topaloğlu's Contributions

I have extended Michael Niemeyer's original script with the following features:

1.  **Dedicated Projects Section:** Projects are now managed in a separate file (`projects.bib`) and automatically rendered on the homepage.
2.  **Equal Contribution Support:** Added support for marking equal contribution co-authors using the `equal_contribution` field in the BibTeX entry.
3.  **Image Linkage:** Clicking on publication/project thumbnail images now automatically directs the user to the associated project page, video, or PDF (based on availability priority).
4.  **Mobile Layout Optimizations:**
 On mobile screens, the profile image is moved to appear immediately below the name/title, before the bio text. Profile picture, publication and project thumbnails are centered and constrained in size for better viewing on small screens. Optionally added name pronunciation guide below the main title.

## How to use it

1.  Update and adjust the name and bio text in the function `get_personal_data` in the `index_generator.py` file.
2.  Upload your own profile photo to `assets/img/profile.jpg`.
3.  Replace `publication_list.bib` with your publications.
    *   *Note:* Entries are crawled from top to bottom.
    *   The script uses additional fields like `html`, `code`, `video`, and `equal_contribution`. Check the function `get_paper_entry` in `index_generator.py` for details.
4.  Replace `projects.bib` with your personal projects (if applicable).
5.  Replace `talk_list.bib` with your talks (if applicable). Check out the function `get_talk_entry` in `index_generator.py` for more information on accepted talk fields.
6.  Update the author websites in the function `get_author_dict` in `index_generator.py` to automatically generate the links to your co-authors' websites.
7.  Run `python index_generator.py` which automatically generates the `index.html` file—the only file you need!
8.  Add credits and a link to the original template creator (Michael Niemeyer) and optionally to this repository.

## Credits

The overall design and open-sourcing the script is inspired by [Jon Barron's awesome template](https://jonbarron.info/) and some functionality is inspired by [Andreas Geiger's cool website](https://cvlibs.net)!

The base script and template were provided by [Michael Niemeyer](https://m-niemeyer.github.io/).