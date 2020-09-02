from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)

info = [
    {
        "id": 1,
        "name": "Belleau Wood",
        "image": "https://www.marines.com/content/dam/marines-com/who-we-are/legacy/battles-through-time/Belleau_Wood-Z3-image1-700x610.jpg.img.full.low.jpg/1490045752063.jpg",
        "alt": "This is a video of the Battle of Belleau Wood",
        "text": "<span class=\"thispage\">June 1 - 26, 1918</span><br><br>4th Marine Brigade <br><br>Fighting against the German, the French wanted to retreat. U.S. Marine Captain Lloyd W. Williams responded: \"Retreat? Hell, we just got here!\"<br><br> Marines fixed bayonets and carried out several charges throughout June. <br><br>Germans referred to the Marines as <span class=\"thispage\">Teufelhunden</span>, meaning Devil Dogs",
    },
    {
        "id": 2,
        "name": "Iwo Jima",
        "image": "https://www.marines.com/content/dam/marines-com/who-we-are/legacy/battles-through-time/jw2943_IWO-Z3-image2-700x610.jpg.img.full.low.jpg/1545250678694.jpg",
        "alt": "This is an image of the Battle of Iwo Jima",
        "text": "<span class=\"thispage\">Feb. 19, 1945</span> <br><br>4th and 5th Marine Divisions <br><br>Fought for 35 days, raised the flag on Mt. Suribachi in this iconic photograph <br><br>Fleet Admiral Chester Nimitz offered the tribute, Among the men who fought on Iwo Jima, uncommon valor was a common virtue.",
    },
    {
        "id": 3,
        "name": "Chosin Reservoir",
        "image": "https://www.marines.com/content/dam/marines-com/who-we-are/legacy/battles-through-time/Korean_War-Z3-image3-700x610.jpg.img.full.low.jpg/1545250702101.jpg",
        "alt": "This is an image of the Battle of Chosin Reservoir",
        "text": "1950 <br><br>1st Marine Division <br><br>Surrounded by Chinese troops and outnumbered 8 - 1, temperatures reached -40 degrees F<br><br> \"Great. Now we can shoot at those bastards from every direction.\" - Chesty Puller<br><br> Decimated 10 Chinese Infantry Divisions while fighting to rejoin American forces",
    },
    {
        "id": 4,
        "name": "Battle of Hue",
        "image": "https://www.marines.com/content/dam/marines-com/who-we-are/legacy/battles-through-time/Hue2-Z4-image1-700x610.jpg.img.full.low.jpg/1545250654228.jpg",
        "alt": "This is an image of the Battle of Hue",
        "text": "1968 <br><br>Began with the Tet Offensive when the Communist forces attacked on the first night of the Vietnamese Lunar New Year<br><br>33 days of Urban warfare until Marines secured victory on March 2<br><br>Intense house-to-house street fighting foreshadowed the tactics Marines would use in Fallujah",
    },
    {
        "id": 5,
        "name": "Second Battle of Fallujah",
        "image": "https://www.youtube.com/watch?v=PC5q3GjYUac",
        "alt": "This is an image of the Second Battle of Fallujah",
        "text": "December 2004<br><br>Bloodiest battle involving American troops since the Vietnam War<br><br>Many civilians were able to leave before the attack",
    },
    {
        "id": 6,
        "name": "Lt. General Lewis B. \"Chesty\" Puller",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Chesty-puller.jpg",
        "alt": "This is an image of Chesty",
        "text": "Most decorated Marine<br><br>Earned 5 Navy Crosses <br><br> Earned first two Navy Crosses in Nicaragua <br><br> Earned the third and fourth in WWII - fourth at the Battle of Guadalcanal <br><br>Earned fifth Navy Cross in the Korean War at the Chosin Reservoir",
    },
    {
        "id": 7,
        "name": "Sergeant Major Daniel Daly",
        "image": "data:image/jpeg;base64,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",
        "alt": "This is an image of Dan Daly",
        "text": "Earned two Medal of Honors - Boxer Rebellion and Haiti<br><br>At the Battle of Belleau Wood, he rallied his Marines by yelling \"Come on, you sons of bitches, do you want to live forever?\"",
    },
    {
        "id": 8,
        "name": "Major General Smedley Butler",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/54/SmedleyButler.jpeg",
        "alt": "This is an image of Smedley Butler",
        "text": "Earned two Medal of Honors - Dominican Republic and Haiti<br><br> Led Marines in the final occupation of Vera Cruz, Mexico in 1914<br><br> Led the attack on Fort Riviere, Haiti in 1915",
    },
    {
        "id": 9,
        "name": "Gunnery Sergeant John Basilone",
        "image": "https://www.armytimes.com/resizer/ZUwFY7VpVyBUvXnOZO6RGDqNZmI=/800x0/filters:quality(100)/arc-anglerfish-arc2-prod-mco.s3.amazonaws.com/public/YF3PZQXNHJCOPKZQY6JV4C6SW4.jpg",
        "alt": "This is an image of John Basilone",
        "text": "Earned the Medal of Honor for his actions in Guadalcanal<br><br> Killed at least 38 enemy soldiers by himself using a machine gun, a pistol and a machete<br><br>Earned the Navy Cross and Purple Heart for his actions in Iwo Jima <br><br>Killed by artillery on Iwo Jima after leading his Marines on the beach and destroying a blockhouse",
    },
    {
        "id": 10,
        "name": "Gunnery Sergeant Carlos Hathcock",
        "image": "https://d26horl2n8pviu.cloudfront.net/link_data_pictures/images/000/283/813/shared_link/carlos-hathcock.jpg?1524270931",
        "alt": "This is an image of Hathcock",
        "text": "93 confirmed kills during the Vietnam War<br><br>Crawled over 1,500 yards over the course of four days and three nights without sleep to kill an enemy general <br><br> Earned Purple Heart and Silver Star after pulling 7 Marines from a burning vehicle<br><br>",
    },
        {
        "id": 11,
        "name": "Eagle, Globe and Anchor",
        "image": "https://www.gettysburgflag.com/blog/wp-content/uploads/2017/01/Marine-Corps-Emblem.jpg",
        "alt": "This is an image of the EGA",
        "text": "Official emblem and insignia of the Marine Corps<br><br>Eagle - symbol of America and carries banner that reads “Semper Fidelis” <br><br> Globe - Signifies worldwide commitment of the Marines<br><br>Anchor - Represents amphibious nature of Marine Corps",
    },
        {
        "id": 12,
        "name": "Blood Stripe",
        "image": "https://www.usmcmuseum.com/uploads/6/0/3/6/60364049/__1454386849.png",
        "alt": "This is an image of Hathcock",
        "text": "Red stripe on the trousers of Officers and Noncommissioned Officers <br><br>Commemorates the Marines killed in the Battle of Chapultepec in 1847 <br><br>Symbolizes honor for all fallen Marines",
    },
        {
        "id": 13,
        "name": "Marine Corps Birthday",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Sketch_of_Tun_Tavern_in_the_Revolutionary_War.jpg/1200px-Sketch_of_Tun_Tavern_in_the_Revolutionary_War.jpg",
        "alt": "This is an image of Tun Tavern",
        "text": "November 10, 1775<br><br>Captain Samuel Nicholas was the first Commandant of the Marine Corps <br><br>Recruited others at Tun Tavern in Philadelphia",
    },
        {
        "id": 14,
        "name": "Core Values",
        "image": "https://pbs.twimg.com/media/BfrAiRbIIAEkZOW.jpg",
        "alt": "This is an image of the Core Values",
        "text": "Honor - Integrity to do the right thing even when no one is looking<br><br>Courage - Strength to persevere <br><br>Commitment - Devotion to the Corps and country",
    },
        {
        "id": 15,
        "name": "Montford Point Marines",
        "image": "data:image/jpeg;base64,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",
        "alt": "This is an image of the Montford Point Marines",
        "text": "First African Americans to enlist in the Marine Corps <br><br> Trained at Camp Montford in Jacksonville, NC from 1942 until it was decommissioned in 1949",
    },
    {
        "id": 16,
        "name": "That's everything!",
        "image": "https://www.armytimes.com/resizer/WHkOAzcKdPGnynlzOOZ9cfZaZgk=/1200x0/filters:quality(100)/arc-anglerfish-arc2-prod-mco.s3.amazonaws.com/public/GOJDETJCBVFJ3I2NFIA6B6SELU.jpg",
        "alt": "This is an image of a Drill Instructor",
        "text": "Click next to go back to the beginning, or go to the quiz to test your knowledge!",
    },
]


@app.route('/')
def home_search():
    return render_template('navbar.html', id=1)

@app.route('/learn')
def learn():
    global info
    name = info[0].get('name')
    image = info[0].get('image')
    alt = info[0].get('alt')
    text = info[0].get('text')
    return render_template('view.html', id=1, name=name, text=text, pic = image, alt = alt)

@app.route('/view/None')
def view1(id=None):
    return


@app.route('/view/<id>')
def view(id=None):
    if id==None:
        id=1
    global info
    print(id)
    print(type(id))
    print(type(int(id)))
    found = False
    x = 0
    for i in range(len(info)):
        print(info[i]['id'])
        if info[i]['id'] == int(id):
            found = True
            x = i
            break
    print(x)
    if x==4:
        name = info[x].get('name')
        vid = info[x].get('image')
        alt = info[x].get('alt')
        text = info[x].get('text')
        id = info[x].get('id')
        print("returned view2")
        return render_template('view2.html', id=id, name=name, text=text, alt = alt)
    name = info[x].get('name')
    image = info[x].get('image')
    alt = info[x].get('alt')
    text = info[x].get('text')
    id = info[x].get('id')
    return render_template('view.html', id=id, name=name, text=text, pic = image, alt = alt)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', id=1)

@app.route('/question1')
def question1():
    return render_template('question1.html', id=1)

@app.route('/question2')
def question2():
    return render_template('question2.html', id=1)

@app.route('/question3')
def question3():
    return render_template('question3.html', id=1)

@app.route('/question4')
def question4():
    return render_template('question4.html', id=1)

@app.route('/question5')
def question5():
    return render_template('question5.html', id=1)



if __name__ == '__main__':
    app.run(debug=True)
