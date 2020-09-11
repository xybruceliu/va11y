import pandas as pd
import numpy as np

def format():
    filename = "user_study_videos.csv"
    df = pd.read_csv(filename)

    for index, row in df[20:30].iterrows():

        #print(str(index)+"==================================")

        duration = str(row["duration"])[2:4] + " minutes " + str(row["duration"])[5:] + " seconds, "

        raw_html = ('<a href="' + row["link_timestamped"] + 
                    '"\ntitle="by ' + row["author"] + ", " + duration + str(row["views"]) + ' views.">\n' + 
                    row["title"] + '\n' +
                    "</a>\n" + 
                    "<p>\n" + 
                    row["description"] + '\n' +
                    "</p>\n")
        
        print(raw_html)


        speech = ""
        # if not descriptive and many visual ref
        if ((row["2_%low_lexical_density"] > 0) and (row["7_#visual_ref"] >= 2.5)):
            speech = "Parts of the speech are not descriptive, and has many visual references (" + str(round(row["7_#visual_ref"])) + " per minute).\n"

        if ((row["2_%low_lexical_density"] > 0) and (row["7_#visual_ref"] < 2.5)):
            speech = "Parts of the speech are not descriptive, the speech has few visual references (" + str(round(row["7_#visual_ref"])) + " per minute).\n"

        if ((row["2_%low_lexical_density"] == 0) and (row["7_#visual_ref"] < 2.5)):
            speech = "The speech is descriptive, and has few visual references (" + str(round(row["7_#visual_ref"])) + " per minute).\n"

        if ((row["2_%low_lexical_density"] == 0) and (row["7_#visual_ref"] >= 2.5)):
            speech = "The speech is descriptive, but has many visual references (" + str(round(row["7_#visual_ref"])) + " per minute).\n"


        visual_change = "not frequently"
        if (row["3_shot_per_min"] > 17.43):
                visual_change = "frequently"

        visual_objects = "few"
        if (row["5_%visual_entities_not_in_speech"] < 0.78):
                visual_objects = "many"

        metrics = (('<p>\n' + 
                    'Prediction: ' + row["pred_a11y_class"] + " (" + str(row["pred_a11y_score"]) + "/" + "7).\n"
                    "</p>\n" ) +
                    ('<p>\n' + str(round((1-row['1_%non_speech'])*100)) + '% of the audio is speech.\n'  + 
                    speech + 
                    "Visual changes occur " + visual_change + " (" + str(round(row["3_shot_per_min"])) + " shots per minute); " + 
                    visual_objects + " of the on-screen objects are described" + " (" + str(round((1-row["5_%visual_entities_not_in_speech"])*100)) + "%).\n"+
                    "</p>\n" ))

        print(metrics)
 

format()
