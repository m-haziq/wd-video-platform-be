from .models import Video, Tag


def generate_test_data_service():

    # create some of the tags for testing
    tag1 = Tag.objects.create(name="Music")
    tag2 = Tag.objects.create(name="Cooking")
    tag3 = Tag.objects.create(name="Travel")
    tag4 = Tag.objects.create(name="Dance")
    tag5 = Tag.objects.create(name="Docker")
    tag6 = Tag.objects.create(name='Programming')
    tag7 = Tag.objects.create(name="Sports")
    tag8 = Tag.objects.create(name="Art")
    tag9 = Tag.objects.create(name="Technology")
    tag10 = Tag.objects.create(name="Health")

    # create videos for testing
    video_1 = Video.objects.create(
        url="https://www.youtube.com/watch?v=igJgH9BuT9I&ab_channel=K%C9%99ndH%C9%99yat%C4%B1",
        title="Whole Bull Leg Tushonka Cooking"
    )

    video_2 = Video.objects.create(
        url="https://www.youtube.com/watch?v=lmma2zxC3dI&ab_channel=K%C9%99ndH%C9%99yat%C4%B1",
        title="Beef Pilaf - Cooked in Clay Pots"
    )

    video_3 = Video.objects.create(
        url="https://www.youtube.com/watch?v=3w6u7ydd5tg&ab_channel=DaisBook",
        title="Tu Subha Di Paak Hawa Warga | Nimra Mehra"
    )

    video_4 = Video.objects.create(
        url="https://www.youtube.com/watch?v=ElZfdU54Cp8&ab_channel=ZeeMusicCompany",
        title="Apna Bana Le - Bhediya"
    )

    video_5 = Video.objects.create(
        url="https://www.youtube.com/watch?v=R_k87larwGI&ab_channel=MattandJulia",
        title="Traveling to the HAPPIEST Country in the World"
    )

    video_6 = Video.objects.create(
        url="https://www.youtube.com/watch?v=RHSwO-FTyCA&ab_channel=DhruvRatheeVlogs",
        title="Travelling to Africa's Richest Country."
    )

    video_7 = Video.objects.create(
        url="https://www.youtube.com/watch?v=EVF_AuhJgLg&ab_channel=SICKVED",
                        title="Non-Stop Road Trip Jukebox")

    video_8 = Video.objects.create(
        url="https://www.youtube.com/watch?v=5U0aoZU7mU4&ab_channel=FlavourTrip",
                                  title="Groovy Deep House Music Mix")

    video_9 = Video.objects.create(
        url="https://www.youtube.com/watch?v=O9ouhTy2QBU&ab_channel=TheHealthNerd",
                                  title="How to Stay Motivated to Lose Weight")

    video_10 = Video.objects.create(
        url="https://www.youtube.com/watch?v=ENKBnhyf4X0&ab_channel=Fopheii",
                                   title="Astronomia Shuffle Dance")

    video_11 = Video.objects.create(
        url="https://www.youtube.com/watch?v=pTFZFxd4hOI",
                                   title="Docker Tutorial for Beginners")

    video_12 = Video.objects.create(
        url="https://www.youtube.com/watch?v=eKqY-oP1d_Y",
                                   title="How to Start Coding? Learn Programming for Beginners")

    video_13 = Video.objects.create(
        url="https://www.youtube.com/watch?v=kqtD5dpn9C8",
                                   title="Python for Beginners - Learn Python in 1 Hour")

    video_14 = Video.objects.create(
        url="https://www.youtube.com/watch?v=kE7D7qFayVg",
        title="Greatest Sports Moments - M83 Outro")

    video_15 = Video.objects.create(
        url="https://www.youtube.com/watch?v=xSsiS304iY8",
        title="Football Matches That Shocked The World"
    )

    video_16 = Video.objects.create(
        url="https://www.youtube.com/watch?v=BCFClUl8Kzw",
        title="Unbelievable Run Chase By Pakistan | Pakistan vs West Indies | PCB | MA2T"
    )

    video_17 = Video.objects.create(
        url="https://www.youtube.com/watch?v=5jQxUBZPuZQ", title="Making Custom Wall Decor")

    video_18 = Video.objects.create(
        url="https://www.youtube.com/watch?v=MaFv-SMgHb0&t=16s",
        title="Depression, Anxiety, Stress & Mental Health Awareness In Hindi"
    )

    video_19 = Video.objects.create(
        url="https://www.youtube.com/watch?v=1COu1d3UOPk&t=12s",
        title="Top 50 Satisfying Videos of Workers Doing Their Job Perfectly"
    )

    video_20 = Video.objects.create(
        url="https://www.youtube.com/watch?v=IJM3yuIDDPQ",
        title="Technology Evolution | 100,000 BC - 2020"
    )

    # assign tags to videos for testing
    video_1.tags.add(tag1, tag2)
    video_2.tags.add(tag2)
    video_3.tags.add(tag1)
    video_4.tags.add(tag1)

    video_5.tags.add(tag3)
    video_6.tags.add(tag3)
    video_7.tags.add(tag1, tag3)
    video_8.tags.add(tag1, tag2)
    video_9.tags.add(tag1, tag2)
    video_10.tags.add(tag1, tag4)

    video_11.tags.add(tag5)
    video_12.tags.add(tag6, tag5)
    video_13.tags.add(tag6, tag5)
    video_14.tags.add(tag7)
    video_15.tags.add(tag7)
    video_16.tags.add(tag7)
    video_17.tags.add(tag8)
    video_18.tags.add(tag10)
    video_19.tags.add(tag9)
    video_20.tags.add(tag9)

    return
