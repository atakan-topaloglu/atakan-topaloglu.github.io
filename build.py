from pybtex.database.input import bibtex
import urllib.parse

def get_personal_data():
    name = ["Atakan", "Topaloğlu"]
    email = "atopaloglu@ethz.ch"
    github = "atakan-topaloglu"
    linkedin = "atakan-topaloglu"
    bio_text = f"""
                <p>
                    I'm a first-year MSc Student in Electrical Engineering and Information Technology at <b>ETH Zürich</b> working on <b>3D Vision</b>, working as a Research Assistant in the <a href="https://prs.igp.ethz.ch/" target="_blank">Photogrammetry and Remote Sensing Lab </a> supervised by <a href="https://scholar.google.com/citations?user=FZuNgqIAAAAJ&hl=en" target="_blank">Prof. Konrad Schindler</a>.
                    Prior to this, I spent three years at <b>Siemens</b> during my undergraduate studies, where I had the pleasure of contributing to engaging projects alongside highly talented colleagues as a R&D Working Student.

                </p>
                <p>For any inquiries, feel free to reach out to me via mail!</p>
                <p>
                    <a href="https://atakan-topaloglu.github.io/assets/pdf/Atakan_Topaloglu_Resume.pdf" target="_blank" style="margin-right: 5px"><i class="fa fa-address-card fa-lg"></i> CV</a>
                    <a href="mailto:atopaloglu@ethz.ch" style="margin-right: 5px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://scholar.google.com/citations?user=l9mFndIAAAAJ&hl=en" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/atakan-topaloglu" target="_blank" style="margin-right: 5px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/atakan-topaloglu" target="_blank" style="margin-right: 5px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                    <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#demo" data-toggle="collapse" style="margin-left: -6px; margin-top: -2px;"><i class="fa-solid fa-trophy"></i>Awards</button>
                    <div id="demo" class="collapse">
                    <span style="font-weight: bold;">Awards:</span>
                      <ul>    
                   <li> In 2024, I was awarded the <a href="https://signalprocessingsociety.org/community-involvement/sps-scholarship-program" target="_blank">IEEE Signal Processing Society Scholarship </a> as the <b>first ever recipient from a Turkish University</b>. </li>
                   <li> We were awarded the best graduation project award on our work on Single-Image-Super-Resolution Evaluation Methodologies under the supervision of <a href="https://scholar.google.com/citations?user=GzwcDjUAAAAJ&hl=en" target="_blank">Prof. Murat Tekalp</a>. </li>
                   <li> I gratefully thank the Hisar Educational Foundation for supporting my undergraduate studies with their scholarship. </li>
                    </ul>


                </div>
                </p>
    """
    footer = """
      """
    return name, bio_text, footer

def get_author_dict():
    return {
        'A. Murat Tekalp': 'https://scholar.google.com.tr/citations?user=GzwcDjUAAAAJ&hl=en',
        'Federico Tombari': 'https://federicotombari.github.io/',
        'Cansu Korkmaz': 'https://mandalinadagi.github.io/',
        'Ahmet Bilican': 'https://scholar.google.com/citations?user=y9uameUAAAAJ&hl=en',
        'Marc Pollefeys': 'https://people.inf.ethz.ch/pomarc/',
        'Kunyi Li': 'https://campus.tum.de/tumonline/ee/ui/ca2/app/desktop/#/pl/ui/$ctx/visitenkarte.show_vcard?$ctx=design=ca2;header=max;lang=de&pPersonenGruppe=3&pPersonenId=6EC78DAA25310FF2',
        'Nassir Navab': 'https://www.professoren.tum.de/en/navab-nassir',
        'Michael Niemeyer': 'https://m-niemeyer.github.io/',
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Atakan Topaloglu', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        name_parts = p.get_part('first') + p.get_part('middle') + p.get_part('last')
        string_part_i = " ".join(name_parts)
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 1.5em;"> <div class="row"><div class="col-sm-3">"""
    
    # Determine the link for the image based on priority: html -> video -> pdf
    image_link = None
    if 'html' in entry.fields.keys():
        image_link = entry.fields['html']
    elif 'video' in entry.fields.keys():
        image_link = entry.fields['video']
    elif 'pdf' in entry.fields.keys():
        image_link = entry.fields['pdf']
    
    if image_link:
        s += f"""<a href="{image_link}" target="_blank"><img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image"></a>"""
    else:
        s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<b><a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span></b><br>"""
    else:
        s += f"""<b><a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a></b> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year']:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 1.5em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')

    if len(bib_data.entries) == 0:
        return ""

    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_project_data():
    return [
        {
            'title': '3D Semantic Segmentation with SAMv2 Memory Bank',
            'description': """
               We noticed that <a href="https://github.com/weijielyu/Gaga" target="_blank">Gaga</a> by Lyu et al. repeatedly labeled the same objects when revisiting regions, especially textureless regions, such as walls, failing to maintain consistency across views. To address this, we leveraged the existing SAMv2 memory bank and used our dense images and pose-based image warping combined with IoU matching to project previous masks onto new viewpoints. This simple approach enforced mask consistency in indoor scenes with "loop closure", reducing duplicate labeling especially in textureless regions.
            """,
            'img_src': 'assets/img/project/3dgs_gaga.png',
            'video_url': '', # nice try!
            'is_private': True,
        },
        {
           'title': '3D Gaussian Splatting from Smartphone Cameras',
            'description': 'We found that aggressive downsampling and color palette quantization of input images had minimal effect on Gaussian Splatting quality in indoor scenes. Leveraging this insight, we redesigned the data pipeline to apply these steps after structure-from-motion (SfM), reducing memory consumption by 83%. In addition, a lightweight interface was developed to make the pipeline accessible for everyday captures from smartphone cameras, lowering the barrier for SMEs and non-expert users to generate their own splats. The final model was reconstructed with maximum GPU VRAM utilization of 3.9 GB from 729 images, occupying 122 MB on disk.',
            'img_src': 'assets/img/project/3dgs_compress_smartphone.png',
            'video_url': '', 
            'is_private': True,
        },
        {
            'title': 'Building Information Modelling (BIM) PoC on CPU',
            'description': 'Developed a proof-of-concept for a Building Information Modeling viewer designed to run efficiently on consumer-grade hardware. This demonstration runs smoothly on an 8th GenIntel i5 CPU (4 cores, 8 GB RAM, 2.8 GHz) with no dedicated GPU.',
            'img_src': 'assets/img/project/3dgs_bim.png',
            'video_url': '', 
            'is_private': True,
        }
    ]

def get_project_entry(project):
    s = """<div style="margin-bottom: 1.5em;"> <div class="row"><div class="col-sm-3">"""
    
    # Determine the link for the thumbnail: public videos or websites only
    thumbnail_link = project.get('website_url')
    if not project.get('is_private'):
        thumbnail_link = thumbnail_link or project.get('video_url')
    
    if thumbnail_link:
        s += f"""<a href="{thumbnail_link}" target="_blank"><img src="{project['img_src']}" class="img-fluid img-thumbnail" alt="Project image"></a>"""
    else:
        s += f"""<img src="{project['img_src']}" class="img-fluid img-thumbnail" alt="Project image">"""

    s += """</div><div class="col-sm-9">"""
    s += f"""<p style="font-weight: bold; margin-bottom: 0.5em;">{project['title']}</p>"""
    s += f"""<div>{project['description']}</div>"""
    
# Generate links, handling private videos
    links = []
    if project.get('is_private'):
        _, personal_data, _ = get_personal_data()
        links.append(f'<a href="https://forms.gle/ZJ55t5bhZ2yUvYeB8">Request Access via Form</a>')
    elif 'video_url' in project:
        links.append(f'<a href="{project["video_url"]}" target="_blank">Video</a>')

    if project.get('website_url'):
        links.append(f'<a href="{project["website_url"]}" target="_blank">Project Page</a>')

    s += ' / '.join(links)
    
    s += """ </div> </div> </div>"""
    return s


def get_projects_html():
    project_data = get_project_data()
    if not project_data:
        return ""
    
    s = ""
    for project in project_data:
        s += get_project_entry(project)
    return s


def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    projects = get_projects_html()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico?v=5">
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-10">
                <div class="row" style="margin-top: 1.5em;">
                    <div class="col-sm-12" style="margin-bottom: 0em;">
                    <h3 class="display-4" style="text-align: center; margin-bottom: 0.3em;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
                    <p style="text-align: center; font-size: 0.8rem; color: #6c757d; margin-top: -10px;">(AH-tah-kahn TOH-pah-loh-loo)</p>
                    </div>
                    <br>
                    <div class="col-md-10" style="">
                        {bio_text}
                    </div>
                    <div class="col-md-2" style="">
                        <img src="assets/img/profile.jpg" class="img-thumbnail" width="280px" alt="Profile picture">
                    </div>
                </div>
                
                <hr style="border: none; border-top: 1px solid #eaeaea; margin: 1em 0; opacity: 0.3;">

                <div class="row" style="margin-top: 1em;">
                    <div class="col-sm-12" style="">
                        <h4>📚 Publications</h4>
                        {pub}
                    </div>
                </div>"""
    if projects:
        s += f"""
                <hr style="border: none; border-top: 1px solid #eaeaea; margin: 1em 0; opacity: 0.3;">
                 <div class="row" style="margin-top: 1.5em;">
                     <div class="col-sm-12" style="">
                     <h4>💻 Projects</h4>
                        {projects}
                    </div>
                </div>"""
    if talks:
        s += f"""
                <hr style="border: none; border-top: 1px solid #eaeaea; margin: 1em 0; opacity: 0.3;">
                 <div class="row" style="margin-top: 1.5em;">
                     <div class="col-sm-12" style="">
                       <h4>🎤 Talks & Presentations</h4>
                         {talks}
                     </div>
                </div>"""
    s += f"""
                    </div>
                </div>
                <hr style="border: none; border-top: 1px solid #eaeaea; margin: 1em 0; opacity: 0.3;">
                <div class="row" style="margin-top: 1em;">
                    <div class="col-sm-12" style="">
                    <div style="background: #f0f0f0; border-radius: 8px; padding: 1em 1em 1em 1em; margin-top: 2em; margin-bottom: 1em; box-shadow: 0 2px 8px rgba(0,0,0,0.05); text-align: center;">
                        <span style="font-size: 1.1em; color: #505050;">
                            The overall design is inspired by and built upon
                            <a href="https://m-niemeyer.github.io/" target="_blank" style="font-weight: bold; color: #007bff; text-decoration: underline;">Michael Niemeyer's cool website</a>.
                        </span>
                    </div>
                    </div>
                </div>
            </div>
            <div class="col-md-1"></div>
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')
