import wikipedia as wiki
import pyttsx3 as ps3

# def something_idk():
#     result = wiki.search('USA');
#     for each in result:
#         try:
#             print(wiki.page(each).summary);
#         except Exception:
#             pass

result = wiki.summary('Humans');

engine = ps3.init();

engine.setProperty('rate', 180);
engine.say(result);

engine.runAndWait();

