from django.shortcuts import render
import markdown
from pathlib import Path
from django.shortcuts import redirect

def index(request, page):

    pages = [
        'about',
        'start',
        'why',
        'comfort',
        'legs',
        'hands',
        'back',
        'chest',
        'shoulders',
        'head',
        'exercises',
        'sources',
        'contact',
    ]

    try:

        # check whether submitted page exists
        # in the above list of pages
        pages.index(page)

    except:

        return redirect('/')

    else:

        BASE_DIR = Path(__file__).resolve().parent.parent
        path = str(BASE_DIR) + '/templates/pages/' + page + '.mkd' 
        mkd_file = open(path, 'r', encoding='utf-8')
        mkd = mkd_file.read()
        html = markdown.markdown(mkd)

        context = {
            'page': page,
            'html': html,
            }

        return render(request, 'layout.html', context)
