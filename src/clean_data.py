from utility_functions import *

data = unpickle("0_companies_data_pd")
write_file(data.iloc[1,0], "trial.txt")
import re
clean_js = re.compile("<script.*?>.*?</script>")
clean_tags = re.compile("<.*?>")
clean_braces = re.compile("{.*?}")
clean_spaces = re.compile("\s+")
clean_special_symbols = re.compile("&\S*?;")
a=clean_js.sub(" ", data.iloc[1,0])
b=clean_tags.sub(" ", a)
c=clean_braces.sub(" ", b)
d=clean_spaces.sub(" ", c)
e=clean_special_symbols.sub(" ", d)
write_file(e, "trial1.txt")