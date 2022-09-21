from abc import abstractmethod
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from trpgassistant.forms  import LoginForm, RegisterForm, ProfileForm
from trpgassistant.models import Profile, CharacterCOC
from django.http import Http404, HttpResponse

import json

def title_action(request):
    context = {}
    if request.method == "GET":
        return render(request, 'trpgassistant/title.html', context)
    elif request.POST['button'] == 'register':
        return redirect(reverse('register'))
    elif request.POST['button'] == 'login':
        return redirect(reverse('login'))


def login_action(request):
    context = {}

    if request.method == 'GET':
        context['form'] = LoginForm()
        return render(request, 'trpgassistant/login.html', context)

    form = LoginForm(request.POST)
    context['form'] = form

    if not form.is_valid():
        return render(request, 'trpgassistant/login.html', context)

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    login(request, new_user)
    return redirect(reverse('frontpage'))


def register_action(request):
    context = {}

    if request.method == 'GET':
        context['form'] = RegisterForm()
        return render(request, 'trpgassistant/register.html', context)

    form = RegisterForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'trpgassistant/register.html', context)

    new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user.save()

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
    profile = Profile(bio='', user=new_user, picture=None, content_type='image')
    profile.save()
    login(request, new_user)
    return redirect(reverse('frontpage'))


@login_required
def front_action(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'trpgassistant/FrontPage.html', context)
    elif request.POST['button'] == 'join':
        return redirect(reverse('join_game'))
    elif request.POST['button'] == 'create':
        return redirect(reverse('create_character'))
    elif request.POST['button'] == 'view':
        return redirect(reverse('list_characters'))
        
    # TODO
    return render(request, 'trpgassistant/FrontPage.html', context)


@login_required
def create_character_action(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'trpgassistant/create_character.html', context)

    new_character = CharacterCOC(PL=request.user,
                                name=request.POST['name'],
                                birthplace=request.POST['birthplace'],
                                gender=request.POST['gender'],
                                occupation=request.POST['occupation'],
                                residence=request.POST['residence'],
                                age=int(request.POST['age']),
                                strength=int(request.POST['strength']),
                                constitution=int(request.POST['constitution']),
                                dexterity=int(request.POST['dexterity']),
                                size=int(request.POST['size']),
                                power=int(request.POST['power']),
                                appearance=int(request.POST['appearance']),
                                intelligence=int(request.POST['intelligence']),
                                education=int(request.POST['education']),
                                luck=int(request.POST['luck']),
                                current_hit_points=int(request.POST['curr_hp']),
                                current_magic_points=int(request.POST['curr_mp']),
                                current_sanity=int(request.POST['curr_sanity']),
                                temporary_insanity=('temporary_insanity' in request.POST),
                                indefinite_insanity=('indefinite_insanity' in request.POST),
                                major_wound=('major_wound' in request.POST),
                                unconscious=('unconscious' in request.POST),
                                dying=('dying' in request.POST),
                                my_story=request.POST['my_story'],
                                wealth=request.POST['wealth'],
                                items=request.POST['items'],
                                personal_description=request.POST['personal_description'],
                                ideology_beliefs=request.POST['ideology_beliefs'],
                                significant_people=request.POST['significant_people'],
                                meaningful_locations=request.POST['meaningful_locations'],
                                treasured_possessions=request.POST['treasured_possessions'],
                                traits=request.POST['traits'],
                                injuries_scars=request.POST['injuries_scars'],
                                phobias_manias=request.POST['phobias_manias'],
                                arcane_spells=request.POST['arcane_spells'],
                                encounters_with_strange_entities=request.POST['encounters_with_strange_entities'],
                                accounting=int(request.POST['accounting']),
                                anthropology=int(request.POST['anthropology']),
                                appraise=int(request.POST['appraise']),
                                archaeology=int(request.POST['archaeology']),
                                art_craft=int(request.POST['art_craft']),
                                charm=int(request.POST['charm']),
                                climb=int(request.POST['climb']),
                                credit_rating=int(request.POST['credit_rating']),
                                cthulhu_mythos=int(request.POST['cthulhu_mythos']),
                                disguise=int(request.POST['disguise']),
                                dodge=int(request.POST['dodge']),
                                drive_auto=int(request.POST['drive_auto']),
                                elec_repair=int(request.POST['elec_repair']),
                                fast_talk=int(request.POST['fast_talk']),
                                fighting=int(request.POST['fighting']),
                                firearms=int(request.POST['firearms']),
                                first_aid=int(request.POST['first_aid']),
                                history=int(request.POST['history']),
                                intimidate=int(request.POST['intimidate']),
                                jump=int(request.POST['jump']),
                                language=int(request.POST['language']),
                                law=int(request.POST['law']),
                                library=int(request.POST['library']),
                                listen=int(request.POST['listen']),
                                locksmith=int(request.POST['locksmith']),
                                mech_repair=int(request.POST['mech_repair']),
                                medicine=int(request.POST['medicine']),
                                natural_world=int(request.POST['natural_world']),
                                navigate=int(request.POST['navigate']),
                                occult=int(request.POST['occult']),
                                persuade=int(request.POST['persuade']),
                                pilot=int(request.POST['pilot']),
                                psychoanalysis=int(request.POST['psychoanalysis']),
                                psychology=int(request.POST['psychology']),
                                ride=int(request.POST['ride']),
                                science=int(request.POST['science']),
                                sleight_of_hand=int(request.POST['sleight_of_hand']),
                                spot_hidden=int(request.POST['spot_hidden']),
                                stealth=int(request.POST['stealth']),
                                survival=int(request.POST['survival']),
                                swim=int(request.POST['swim']),
                                throw=int(request.POST['throw']),
                                others=int(request.POST['other']),
                                describe=request.POST['describe'])
    new_character.save()
    return redirect(reverse('frontpage'))


def view_character_action(request, id):
    character = get_object_or_404(CharacterCOC, id=id)
    if request.method == "GET":
        context = get_character_context(character)
        return render(request, 'trpgassistant/view_character.html', context)

    character.current_hit_points = int(request.POST['curr_hp'])
    character.current_magic_points = int(request.POST['curr_mp'])
    character.current_sanity = int(request.POST['curr_sanity'])
    character.temporary_insanity = ('temporary_insanity' in request.POST)
    character.indefinite_insanity = ('indefinite_insanity' in request.POST)
    character.major_wound = ('major_wound' in request.POST)
    character.unconscious = ('unconscious' in request.POST)
    character.dying = ('dying' in request.POST)
    character.save()

    context = get_character_context(character)
    return render(request, 'trpgassistant/view_character.html', context)


def get_character_context(character):
    context = {'name': character.name,
                'birthplace': character.birthplace,
                'gender': character.gender,
                'occupation': character.occupation,
                'residence': character.residence,
                'age': character.age,
                'strength': character.strength,
                'constitution': character.constitution,
                'dexterity': character.dexterity,
                'intelligence': character.intelligence,
                'size': character.size,
                'power': character.power,
                'appearance': character.appearance,
                'education': character.education,
                'luck': character.luck,
                'max_hp': int((character.size + character.constitution) / 10),
                'max_mp': int(character.power / 5),
                'max_sanity': character.power,
                'curr_hp': character.current_hit_points,
                'curr_mp': character.current_magic_points,
                'curr_sanity': character.current_sanity,
                'temporary_insanity': character.temporary_insanity,
                'indefinite_insanity': character.indefinite_insanity,
                'major_wound': character.major_wound,
                'unconscious': character.unconscious,
                'dying': character.dying,
                'accounting': character.accounting,
                'anthropology': character.anthropology,
                'appraise': character.appraise,
                'archaeology': character.archaeology,
                'art_craft': character.art_craft,
                'charm': character.charm,
                'climb': character.climb,
                'credit_rating': character.credit_rating,
                'cthulhu_mythos': character.cthulhu_mythos,
                'disguise': character.disguise,
                'dodge': character.dodge,
                'drive_auto': character.drive_auto,
                'elec_repair': character.elec_repair,
                'fast_talk': character.fast_talk,
                'fighting': character.fighting,
                'firearms': character.firearms,
                'first_aid': character.first_aid,
                'history': character.history,
                'intimidate': character.intimidate,
                'jump': character.jump,
                'language': character.language,
                'law': character.law,
                'library': character.library,
                'listen': character.listen,
                'locksmith': character.locksmith,
                'mech_repair': character.mech_repair,
                'medicine': character.medicine,
                'natural_world': character.natural_world,
                'navigate': character.navigate,
                'occult': character.occult,
                'persuade': character.persuade,
                'pilot': character.pilot,
                'psychoanalysis': character.psychoanalysis,
                'psychology': character.psychology,
                'ride': character.ride,
                'science': character.science,
                'sleight_of_hand': character.sleight_of_hand,
                'spot_hidden': character.spot_hidden,
                'stealth': character.stealth,
                'survival': character.survival,
                'swim': character.swim,
                'throw': character.throw,
                'track': character.track,
                'other': character.others,
                'describe': character.describe,
                'my_story': character.my_story,
                'wealth': character.wealth,
                'items': character.items,
                'personal_description': character.personal_description,
                'ideology_beliefs': character.ideology_beliefs,
                'significant_people': character.significant_people,
                'meaningful_locations': character.meaningful_locations,
                'treasured_possessions': character.treasured_possessions,
                'traits': character.traits,
                'injuries_scars': character.injuries_scars,
                'phobias_manias': character.phobias_manias,
                'arcane_spells': character.arcane_spells,
                'encounters_with_strange_entities': character.encounters_with_strange_entities}
    return context


def list_characters_action(request):
    if request.method == "GET":
        return render(request, 'trpgassistant/character_list.html', {'characters': CharacterCOC.objects.order_by("-id")})
    
    character_id = request.POST['button']
    return redirect(reverse('view_character', kwargs={'id': character_id}))


def join_game_action(request):
    if request.method == "GET":
        return render(request, 'trpgassistant/canvas.html', {'characters': CharacterCOC.objects.order_by("-id")})
    
    if request.POST['button'] == 'add':
        return redirect(reverse('add_character'))
    if request.POST['button'] == 'remove':
        return redirect(reverse('remove_character'))

    character_id = request.POST['button']
    return redirect(reverse('view_character', kwargs={'id': character_id}))


def add_character_action(request):
    if request.method == "GET":
        return render(request, 'trpgassistant/add_character_list.html', {'characters': CharacterCOC.objects.order_by("-id")})

    character_id = request.POST['button']
    character = get_object_or_404(CharacterCOC, id=character_id)
    character.in_game = True
    character.save()
    return redirect(reverse('join_game'))


def remove_character_action(request):
    if request.method == "GET":
        return render(request, 'trpgassistant/remove_character_list.html', {'characters': CharacterCOC.objects.order_by("-id")})

    character_id = request.POST['button']
    character = get_object_or_404(CharacterCOC, id=character_id)
    character.in_game = False
    character.save()
    return redirect(reverse('join_game'))



# Used for test
def get_all_characters_action(request):
    characters = []
    for character_item in CharacterCOC.objects.all():
        my_item = {
            'PL': character_item.PL.id,
            'name': character_item.name
        }
        characters.append(my_item)
    response_json = json.dumps(characters)
    response = HttpResponse(response_json, content_type='application/json')
    return response



def add_comment(request):
    if request.method != 'POST':
        return _my_json_error_response("You must use a POST request for this operation", status=405)

    if not request.user.id:
        return _my_json_error_response("You must be logged in to do this operation", status=401)


    if not 'post_id' in request.POST or not request.POST['post_id']:
        return _my_json_error_response("You must be logged in to do this operation", status=400)


    if not 'comment_text' in request.POST or not request.POST['comment_text']:
        return _my_json_error_response("You must enter an item to add.", status=400)

    if not request.POST['post_id'].isnumeric():
        return _my_json_error_response("You must enter an item to add.", status=400)


    try:
        post=Post.objects.get(id=request.POST['post_id'])
        new_item = Comment(comment_by=request.user,comment_is_under_post=post,comment_text=request.POST['comment_text'],comment_time=timezone.now())
        new_item.save()
    except: 
        return HttpResponse("error", content_type='application/json',status=400)

    return get_stream(request, post)