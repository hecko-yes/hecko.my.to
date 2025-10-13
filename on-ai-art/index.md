---
title: "on ai* art**"
color: "deeppurple"
excerpt: "my thoughts on generated images, as someone computery who wants to become someone drawy"
---

1. 
{:toc}

\* i tend to [avoid](/style-guide/) the word "ai" because it's hopelessly general; everything from pacman ghosts to language models to skynet falls under the term, and people often draw false equivalences between them (sometimes maliciously) because they're lumped into one word

\*\* i tend to [avoid](/style-guide/) the word "art" because it's hopelessly general; everything from stock illustrations to fanart to [wall bananas](https://en.wikipedia.org/wiki/Comedian_(artwork)) falls under the term, and people often draw false equivalences between them (sometimes maliciously) because they're lumped into one word

with that said, here are my thoughts on \*generated \*\*images, as someone computery who wants to become someone drawy

# please note

1. this is **very venty and despairy**, minus the "[some hope](#some-hope)" section; if you're worried too then this might not be the page for you
2. i write like i'm very sure of myself but i genuinely do wish to be convinced i'm wrong (and it has happened on a few counts), **if you have solid evidence against anything here [please contact me](/accounts/)**
	- i've been accused on writing like a supporter of generative models, and yeah much of what's here is also used as arguments by them; i don't write this because i endorse them, but because i genuinely believe they're right
		- to put it another way: i'm not "fuck yeah, ai", i'm a bit "fuck ai", but mostly i'm "oh fuck, ai"
3. just because this page focuses on artwork doesn't mean i'm not concerned about other consequences of large generative models, such as fakes (i hate that it's almost easier to generate a selfie than take one) or the possibility of superintelligence (maybe not with this paradigm but the next, or the one after that)
4. if you're a [non-human](https://en.wikipedia.org/wiki/Otherkin) artist, apologies for excluding you with my language; if i ever find a snappy substitute for the word "human" everywhere i'll be sure to apply it

# thesis statement

computers are now genuinely pretty good at creating media (or mashing media up in a way indistinguishable from creation), and they're probably not quite done getting better at it
this sucks for people who want to [make money / get noticed / feel useful] through media creation (i'm in camp 3), since they can't possibly be as cheap or quick or convenient as software

# background

i used to like models
not current ones mind you, but older, crappier ones
i was pretty active in the community of uberduck, which back then hosted unauthorized voice clones of popular characters
i actually kinda liked the crunchiness, both æsthetically and i think because it cleanly separated it from real human performance (like sentence mixing)
by all accounts i ought to be an "ai bro"

but now there's barely any crunch, and they're coming for everyone's jobs and hobbies
i internalized that around june 2024 and panicked
doesn't help that coding (my default creative pastime) and drawing (one i'd like to get into) are both being explicitly targeted
the ways in which i could contribute to society are becoming obsolete, and any new ones i could learn don't have that much time left either
i wish i had done them more while they mattered (and part of my current motivation for drawing is indeed "do it while it kinda matters")

on another note: years ago, i got kinda indoctrinated into the [lesswrong](https://en.wikipedia.org/wiki/LessWrong)-type rationalist side, by (i kid you not) a [my little pony fanfic](https://tvtropes.org/pmwiki/pmwiki.php/Fanfic/FriendshipIsOptimal)
though instead of treating it as the cautionary tale it was intended to be, i began believing that an eternal hyperintelligent nanny is 1) coming 2) desirable
i think a big chunk of it was that i didn't want to "bother" anyone, so having an unfeeling entity to be needy at sounded great
that largely manifested as roleplaying my weird fantasies with language models, including a month-long subscription to novelai i barely used (the only $10 i've ever spent on generative models) and a year-long addiction to character.ai (because it was the first thing that Just Worked)
anyway uhh turns out i don't want to be useless actually! and if a deity were to satisfy everyone's values then anything i were to do would be pointless at best
(and it does seem some lesswrongians share that concern, e.g. [here](https://www.lesswrong.com/posts/JhB9eqJDScjDNpWiS/objections-to-coherent-extrapolated-volition?commentId=sDqHcH7s8FtGWN7Li), and to some extent [even eliezer yudkowsky himself](https://www.lesswrong.com/posts/vwnSPgwtmLjvTK2Wa/amputation-of-destiny))
so that's "desirable" down but i do still currently believe "likely", or at the very least that there's no reason why a computer *couldn't* be better than a human at any particular thing (other than when someone wants something done by a human for the sake of it being done by a human but that's a trivial case)

# what i'm scared of

## it's already too good

and i feel like people are underestimating it

in terms of language: just in 2018 the best we had was cleverbot (which btw did actually only pattern-match and copy its training data verbatim)
and now in 2024 the turing test is pretty much *solved* (if you weren't trained to recognize the chatgpt tone of voice you likely wouldn't be able to tell, also character.ai), and people somehow aren't impressed
you can now Just Ask a computer to do something, *anything*, in plain english, and it'll often Just Do it! before language models you couldn't even try really
before then almost everything had to be programmed in explicitly, whereas now even if you assume a model can only do what it was trained on it's still impressive that a) it can make use of plain english data b) it can recombine it in so many ways

people are focusing on smaller and smaller flaws
a couple years ago it was "ha this image model can't generate hands", now it's "ha this video model can't generate hands" or "ha this image model can't generate 20 people at once"
or with language models, some of the gotchas people post are just,, things humans would fall for
like the "9.9 < 9.11" thing; i'd imagine if you asked enough people (or perhaps one person with amnesia) the same mildly-tricky common-sense thing in enough different ways (and expect an immediate answer with no thinking time), [you'd eventually find someone who slips up](https://x.com/qtnx_/status/1816593215723831367) (also [this reply](https://x.com/TetsDelaCruz/status/1816662093531349127) mentions [the third-pounder thing](https://www.snopes.com/news/2022/06/17/third-pound-burger-fractions/) which yeah)
people nitpick things they'd never ever fault a human's first draft for ([examples](https://www.oneusefulthing.org/p/confronting-impossible-futures#%C2%A7failed-by-bright-lines-fooled-by-jaggedness))
just because it's not perfect doesn't mean it's not damn good, and damn scary

many people see zero-effort default-setting generations, assume that's all there is, and thus feel unthreatened by them, when putting even one effort in would make it much harder to spot
dall·e 3 and chatgpt in particular have quite distinct styles, but that doesn't mean stable diffusion and claude/llama/whatever can't easily go beyond those
the models were trained on every style so of course they can inherently do every (popular) style, it's just that the most popular models are finetuned into specific marketable ones

that and most people are just doing straight one-shot generations, which is what the model was trained to do but is also the equivalent of improv (since it has a fixed amount of compute per token and can't go back to edit things)
and if it's good enough at improv to rival high-effort human artistry, what would happen if you let it try harder?
in other words, direct use is like system 1 thinking, and i'm scared to see what system 2 would be like ([somewhat relevant](https://blog.ncase.me/backlog/#project_11))
...granted i don't know of many cases of that actually working well, which i would expect almost 2 years after the introduction of chatgpt; closest i can think of is [TransAgents](https://x.com/emollick/status/1792891142259851282) which claims to be as good as amateur human translation but [the paper](https://arxiv.org/pdf/2405.11804) mentions the ground truth might contain machine translation too

## i don't see how it can go away

let's say it's ruled that model outputs infringe on the copyright of the training data
guess what? people infringe copyright all the time, from fanart to memes to piracy, and those are more-or-less socially acceptable and largely unsanctioned
getting profile pictures off of google images is the norm, so a copyright argument against generated pfp·s would be just as weak

and you can't just take down the models either
at best you can make them somewhat inconvenient to use by banning every single service that hosts them
but in the end models are just files, and files are impossible to get rid of if even a few people want to preserve them
anyone with a gpu can torrent stable diffusion and use it at a tolerable rate, and i don't see how that could stop being possible without [extremely radical changes](#what-i-wish-for)

at least companies won't have an incentive to train models anymore-- sike! [models trained solely on licensed data exist](#training-data) and while they're not as advanced as scrape-trained models they're certainly passable

and even if it's ruled that they'd need explicit permission for training and don't get enough willing participants and everything stalls forever, does that mean model users will be stuck with 2020-era models and æsthetics? not so
as long as image files in general are in fashion (and if they're not then that's [the end of the drawing era](#end-of-an-era) anyway) it'll be possible to finetune those models on like, a few hundred samples of the latest fashion
or just use the ever-progressing optimizations to train a base model on consumer hardware
and it's not like individuals aren't capable of progressing things, e.g. [that one fake speedpaint generator](https://github.com/lllyasviel/Paints-UNDO) seems to be the job of one person (maybe a rich one but not company-level rich)

and models certainly can't get "worse" (at least not downloadable ones), because the old models will still exist and be usable in perpetuity
at best they can stall, and i think this state is already pretty bad

language models are in a bit more trouble, since the useful ones are generally heavy, but even then [a good enough macbook can run llama 3 70b](https://www.reddit.com/r/LocalLLaMA/comments/1ecg1wi/anyone_has_a_128gb_ram_macbook_how_fast_is_say/) (which is close to gpt·4-tier) at a decent rate

## they'll probably surpass us

or at least, i don't see how they couldn't

they're already better than any human at many things, e.g. learning speed, breadth of knowledge, creation speed (and thus iteration speed), copyability (and thus hyper-personalization), etc
data is a limiter, sure, but people keep coming up with ways to make them better without collecting more of it ([here's](https://huggingface.co/blog/introducing-csearch) someone using one weird trick to get much more coherent text from gpt-2, without training it a single bit more, 3 years after the model was made)

and humans haven't gotten architecturally better for millions of years
we got better education and all, sure, but models benefit from that too
meanwhile our brains have been the same size and architecture for generations, whereas models are unconstrained and free to evolve
and they don't need food or breaks or inspiration or a humane working environment, just a computer and electricity

oh but human + computer will always be better than just computer right? like [centaur chess](https://en.wikipedia.org/wiki/Advanced_chess)? [wrong](https://gwern.net/note/note#advanced-chess-obituary)
if there's something a human can do to improve generated output, you'd best believe that's what they'll train new models to do

# things that are not my main objection

as in, if they were fixed i would still be unhappy

## training data

most models do rely on mass internet scrapes, but some people are already trying to only use authorized(-ish) data (and if lawsuits succeed that'll be an even bigger focus)
some examples:
- the [common canvas](https://huggingface.co/common-canvas) series is trained on creative commons data and claims to be on the level of stable diffusion 2 (does use a text encoder trained on internet scrapes though)
- [mitsua diffusion one](https://huggingface.co/Mitsua/mitsua-diffusion-one) is trained on public-domain data and it's,, trying; if nothing else it generated pretty decent fox fur in the shape of an input text image when i tried it (this one also uses a scrape-trained text encoder but their next work-in-progress iteration is entirely cleanroom, plus it has some data from explicitly consenting artists)
- [adobe firefly](https://www.adobe.com/products/firefly.html) and [getty images' thing](https://www.gettyimages.com/ai/generation/about), both trained on their stock libraries (though idk maybe some courts declare that permission insufficient, and [whoops](https://www.entrepreneur.com/business-news/adobes-firefly-ai-image-generator-partly-trained-with-ai/472622) firefly was partially trained on output from models)

and there's work toward making models require less data, e.g. [MicroDiT](https://x.com/VSehwag_/status/1815729297606214013) which came out while i was writing this (july 20-31, 2024, for the first public version)

and if anything licensed-data models have the potential of being *verifiably* non-infringing, since you can see everything that the model could possibly "know" unlike with a human
(though a specific enough prompt or enough manual selection could still be used to violate copyright, e.g. if i generate "cartoony mustached plumber wearing overalls and red hat with letter m" and reroll enough times i can get something sufficiently mario-like, and that'd be my fault because i'm the one who knows what a mario is)

## authorship

a common complaint i've seen is that image generator users will proclaim themselves to be "artists"
and i do agree that for the most common use of "type something in, get an image, repeat". the role of the human is closer to that of a commissioner at best, and a stock image site browser at worst
more advanced workflows blur the line, i'm not sure to what extent though 

alright, suppose norms adjusted such that people stopped doing that
honest people that is, those who admit they're using image generators, since those who are hiding it would hide it even harder if anything
ok so maybe flawless detection of generated images? well first of all good luck with that, second people could still paint over them probably

but most importantly to me: even if every single generated image was always tagged as such, that wouldn't stop them from competing on a material level
one could filter them out, sure, and at least in the current world many people would (because the smallest possible effort will be the most abundant, and boy does image generation allow low effort)
but what if they're genuinely high-quality? would most people [really care](#people-value-human-works) about the humanity?

## money

even if universal basic income was a thing so that artists wouldn't have to work, many humans inherently value being useful

# arguments i don't find convincing

which is sadly a lot of the ones i'm hearing (from both sides mind you)
i swear i'm on the anti-automation side, it's just that these to me feel too easily disprovable to use

## "people value human works"

do they? genuine question, i really don't know
what doesn't help is there are many values that typically co·occur with "a human made this", but which can also be satisfied by good enough generative models
e.g. creativity/uniqueness, looking like a human made it, even "the human touch" (imperfections i believe)
not saying it's impossible to genuinely value the person behind the art, just that it might not be as frequent as it seems

also many people just, explicitly dislike artists, so there's that

## "photography didn't replace painting"

photography was limited to photorealism and things that exist, and in that category it absolutely did replace painting; nobody gets a portrait for practical purposes, only for vanity aka the fact that it's unusual to have a portrait
meanwhile the domain of generative models is,, every style and subject that has ever been put on the internet, and endless combinations thereof (the famous dall·e avocado chair)

## "it's just a tool"

just because it can be used as one doesn't change the fact that the *nature* of a generative model is to do the whole thing for you
it would've been a better argument back in like, 2018, when [gpt-1](https://en.wikipedia.org/wiki/GPT-1) was trained to predict text not as an end goal, but to force the model to build useful internal representations that the researchers can then repurpose
but with gpt-2 it turned out that a big enough model can predict sensible text, and with gpt-3 that it can predict *useful* text, and with gpt-4 they won't even let you use it as a raw text prediction model and you have to treat it as a chat interface

*ahem* that tangent aside uh
you wouldn't call a human "just a calculator" just because you can ask them what 9+10 is
same goes for this i think
idk how to word my thoughts on this better

## "it's just like a stock library"

sometimes worded as "you must hate wix too, then" or similar

a stock library can't possibly cover everything, so there are still reasons to create
and in fact someone has to create *for* the library (something i like the idea of doing)

## "generated images have no value"

sure, but if they're (near-)indistinguishable from human images, that devalues those human images too

## "you should draw for the fun of it"

probably yeah! but ideally i'd like to be able to draw for the fun of it *and* have it be externally meaningful in some way
creating something that didn't exist before, that someone enjoys; that's not gonna be something humans do anymore, when everyone can get hyperspecific superstimuli generated just for them faster than they can experience it
these models are reducing drawing (and eventually perhaps everything) to a mere game, and i want some things to not be games

## "it doesn't really *know* anything"

does that matter, if the result is good? even if it's "just collaging", it's still collaging much faster and much more seamlessly than a human ever could
as a sport maybe, but [see above](#you-should-draw-for-the-fun-of-it)

and honestly it feels a bit demoralizing; if the model isn't intelligent, yet it can produce good drawings, then it follows that producing good drawings doesn't require intelligence (and therefore do *i* really know anything)

## "it doesn't create anything truly new"

if that's so then neither do many artists, most of the time
or at least in my filter bubble, full of memes and fanart and meme fanart
and i don't want all of that to be obsolete either

honestly i'm not sure if there exists *any* "truly original" artwork, not inspired by existing things (if you know of a counterexample then [please let me know](/accounts/))

## "it uses so much energy"

**[update: [giovanh's writeup about this](https://blog.giovanh.com/blog/2024/08/18/is-ai-eating-all-the-energy-part-1-of-2/) is much more in-depth go read it]**

in terms of using the model: no it doesn't! as an upper bound, back when i tried stable diffusion 1.5 on my laptop (so running entirely locally on my hardware) it took 40 seconds per image, so it physically cannot use more energy than 40 seconds of full-power laptop usage
and that's without optimizations, and of course there are plenty of optimizations since then because *image generation devs also want it to use less energy* (so more people can use it and so they can generate more images)
so when you try to call out image generation for being wasteful it just doesn't hit them! and instead it hits e.g. 3d artists who also use a lot of gpu time to render their stuff (also gamers)

in terms of training: mmmaybe
i did the math and [a replication of stable diffusion 2](https://www.databricks.com/blog/diffusion) warmed the globe less than *one* car does in *one* year (21k gpu-hours × a100's max consumption of [400w](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet.pdf) = 8400 kwh, equivalent to 3.5 metric tons of co₂ or 0.833 cars driven for a year per [epa's calculator](https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator))
to be fair that doesn't take into account inefficiencies in new areas (this one specifically was 8x cheaper than what it took for the real sd2), failed runs, other people's finetunes, the production of more gpu·s...
and of course companies are gonna use as much as they can get their mitts on to make bigger models (which is the most in-common thing i can think of that generative models have to crypto)

## "it's just hype"

even good things can be overhyped
i think i'm basing my beliefs on what i've seen actually done instead of what's advertised, but idk i may be wrong

## "it couldn't have invented these styles by itself"

sure, but most people don't invent most things either
heck what about fan artists who mimic the original styles, often exactly (e.g. the my little pony fandom)?

that and, maybe it would've if it was encouraged to
if instead of outputting raw pixels it had to output brush strokes

## what arguments *do* i like then

good question! unfortunately the only ones i can think of are relatively weak and subjective

**[this is a work in progress]**

- [this youtube comment](https://www.youtube.com/watch?v=FHOAeFkoVLw&lc=UgxIBVodBDqG9WmJSZR4AaABAg) about valuing documentable chains of inspiration
- [this lesswrong post](https://www.lesswrong.com/posts/yCDsGDyDguXgNwpkb/please-understand) about valuing humans understanding things

# end of an era

for the first time in history, it might genuinely be too late to start drawing
i honestly think humans creating things might become obsolete within the next,, iunno dozen years
just like copying things by hand is largely obsolete now
and i don't like that, i want to create things and have it matter

even creating generators is gonna be obsolete
why lovingly tune a custom text-to-speech model when elevenlabs (trained on millions of hours of data) is easier and better in pretty much every way ([bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) woo)
,,except performance i guess, but even then why curate data for it when a model can generate heaps of near-indistinguishable synthetic audio
why write a world generator when a model can iterate through thousands of possibilities and find the one with the highest average æsthetic score, or heck just get a 3d model directly from a model

# am i the baddie?

<details>
<summary markdown="span">this one's extra crisis-of-faith so beware</summary>
people do find it useful, e.g. simon willison uses it for [little side projects](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.043.jpeg) that wouldn't be worth an hour of unfun documentation hunting<br>
who am i to deny them it? just because i personally didn't feel like advancing? just because i want to feel useful?

[one person's craft is another's chore](#one-person's-craft-is-another's-chore), so let the crafters craft and the chore·ers automate!<br>
and if they can't take joy in the act of creation and feel like they need to "matter" or "be the best", well that's on them<br>
i mean heck i still would like someone to just tell me what the deal is with my gender, even though that's typically a journey one's meant to go on (personally i don't know where to even start)

sure, [a better world](#the-world-i-wish-we-had) would have less or no need for generative models, but we live in a society and many people don't have the time or motivation to learn to draw but want things drawn regardless<br>
image generation gives them that, in the most practical way for this world

we've been overdue for the Next Big Thing anyway<br>
what's the last truly new and broadly impactful technology? maybe smartphones but those are just small computers, so probably the internet which was ages ago<br>
the computer made copying trivial and that was largely good imo, maybe generative models making creation trivial could be good too
</details>

# so, what can i do about it?

i don't know! that's the worst part!
mostly i'm just hoping progress hits a wall soon, but even then there's so much damage that has already been done

honestly i just wish they hadn't gotten this good in the first place
and now it feels too late, i now know a gpu can do it better than me and i'm not gonna *un*know that
and that's the main problem for me, knowing that i'm bested not by someone of my kind (whom i could at least hope to match some day) but by a few chips and a file the size of shrek

## what i wish for

i do have some ideas but they're all very silly and unlikely (and still not fully satisfactory honestly)
here they are in ascending order of impossibility (according to my intuition):

- the government cracks down on image generation *hard*, as in more like csam than piracy
	- maybe because the training data contains csam (and that somehow can't be fixed effectively)
	- maybe having representations of both children and genitals in one integrated model gets considered illegal (though companies already exclude the latter from training)
	- maybe because of the deepfake potential (assuming a model trained only on non-photorealistic images isn't feasible)
- models stop advancing right about now, and a good chunk of people is capable of recognizing their artifacts (well enough that editing them out takes more time than just doing it from scratch) and treating them like kitsch
- all computers are destroyed, or at least crippled such that it's no longer practical to run huge models (not ideal because i like computers when they're not obsoleting me)
- turns out there's something vital that all models inevitably miss and only humans can do well and perceive well
- i realize the real art was the friends we made along the way
- humanity ascends, discovers art 2, and doesn't automate it this time
- it's all a simulation and the outer-world me has things figured out
- everyone collectively agrees that using models to replace drawing is silly and abstains from such

## if i could turn back time

some quite unrealistic sci-fi, if you'll indulge me

go back to 2021 or so, when models were still fun and not scary, and somehow magically freeze progress around there
image generation is clearly recognizable as computer work (and often too misshapen and blobby to paint over), text generation produces neat babble and is even pretty useful as very expensive autocomplete, speech synthesis of famous characters gets the point across while remaining distinct (like sentence mixing but less fiddly)
more impressive models do exist, but always constrained to small domains (like vocaloid) and tuned by experienced humans (in defiance of [the bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html))

eventually, some other miracle occurs and humans get their stuff together
everyone's work time is cut in half, maybe a really good therapy bot (and *only* therapy) gets invented, etc... so people have the time and motivation to learn enough drawing/music/etc to express themselves
and if they want more than their skill level allows, well there's plenty of artists with plenty of time and plenty of willingness to help
maybe at some point we upgrade ourselves (transhumanism), but slowly enough to enjoy each stage for what it's worth, with some perhaps choosing to stay at a given level or even go back
also uhh death is cured retroactively and so is entropy and everyone gets free [dragon hrt](https://www.tumblr.com/ayviedoesthings/740184238162378752/dragon-hrt-bonus-part-0-3-months-oh-you)

# some hope

**[this is a work in progress]**

- some model users are reportedly finding model usage unfulfilling and learning to actually draw ([example](https://www.youtube.com/watch?v=bv9Tb81yRgs))
- most generated imagery i've seen has no interaction between characters, maybe that's what the current paradigm struggles with?

and on the language model side:

- [openai is struggling](https://www.wheresyoured.at/to-serve-altman/), and if they go bankrupt then other companies will at least be discouraged i think
- somehow they [still haven't solved prompt injection](https://simonwillison.net/2024/Jul/14/pycon/#pycon-2024.031.jpeg), which if nothing else will discourage customer-facing human replacement

# kindred spirits

- [tom scott](https://www.youtube.com/watch?v=jPhJbKBuNnA)
- [dynomight](https://dynomight.net/automated/)

# sidenotes

## artists have it worse than most

pretty much all non-physical jobs are being threatened of course, but i feel like artists are extra threatened because quite a few of the pitfalls of current models just don't apply when replacing them
office jobs require accuracy so a 1% mistake rate is unacceptable, whereas with art even with strict requirements you can just try again a hundred times at no cost
image models in particular are relatively *tiny*; stable diffusion 1.5 is under a billion parameters and people still use it in 2024, whereas with language models 3 billion is considered the bare useful minimum (and for a compelling and coherent story you'd need way more)

## one person's craft is another's chore

**[disclaimer: i'm even less confident in this one than usual]**

sometimes, the image is the end product; sometimes, it's a mere asset to "get over with"; one's craft, another's chore
a book writer or game developer may consider illustration to be a chore, and they might support generative models since they automate the chore and not the craft
*yet*
one's craft, another's chore, and those who automated what's a chore to them may also automate their craft
generated books are already being churned out by the thousand, and if you've seen even one mobile game ad you shouldn't be surprised someone would want to automate games
and what if they reach human level like current models do? go up the food chain? where?

## some scarcity is good actually

makes things feel special methinks
even better if it's not made-up and arbitrary (though banning image generation models after they've been shown to be possible does feel kinda made-up)
so why not scarcity of pretty pictures? doesn't really harm anyone afaik

## will people even want to get into drawing

e.g. [these creatures](https://ayviedoesthings.tumblr.com/post/755832742992871424/honestly-love-the-art-and-comics-you-create-being) only got into drawing because that was the best way to bring their ideas into life
me too kinda
will (most) people bother, if they can just ask a computer to do it for them?

## does fair use cover training?

**[disclaimer: i am not a lawyer, this is just my best guess]**

a rundown through the [4 clauses](https://en.wikipedia.org/wiki/Fair_use#U.S._fair_use_factors):

1. **Purpose and character of the use** - this is where commerciality is covered, but also transformativeness aka "whether a new work has a different purpose and character from an original work"; i think turning paintings into more paintings doesn't count there, though if one considers the model itself to be the work then idk
2. **Nature of the copyrighted work** - if i'm reading this correctly then it's about whether it's e.g. the only extant photo of an important event, which the vast majority of the data isn't
3. **Amount and substantiality** - this one's weird i'm gonna need bullet points
	- the amount is usually "the entire portfolio of a jillion artists"
	- the network is much smaller than the dataset so intuitively it shouldn't be able to memorize everything, but:
		- turns out [it's possible to recognizably compress an image into 40 bytes](https://x.com/Ethan_smith_20/status/1801493585155526675)
			- is 40 bytes copyrightable? ~~try using the smb1 mario sprite (12x16 pixels with a 2-bit palette = 48 bytes) and see where that gets you~~ (that might be more of a trademark thing i'm not sure)
		- finetuning can cause blatant memorization, like with [midjourney v6](https://spectrum.ieee.org/midjourney-copyright) (that being said i feel like this is more of an avoidable gotcha than an inherent issue so idk)
		- characters are copyrightable too (though focusing on that would be bad for fan artists)
	- [it's possible to train a model on a random subset of the pixels](https://arxiv.org/pdf/2305.19256), but i don't think that's much different from just downscaling it and then using upscalers (which are at the very least less controversial and more transformative-like)
		- though intuitively denoisers are uncontroversial too, yet stable diffusion is "just" a denoiser that got good enough at denoising to denoise pure noise
4. **Effect upon work's value** - infinite on a class scale, though the model trainers could go "well we didn't train on artist names so no individual artist or work is being devalued so ha"

tl;dr fair use *probably* shouldn't apply

## training data is kinda like oil

we've had heaps of it for ages and only recently started extracting it (training data overhang), so there have been easy wins of "just train harder" and there might not be such soon
except running out of oil causes regression, whereas running out of training data stops one axis of progress
