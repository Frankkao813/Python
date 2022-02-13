'''
imported module: aspose.words
use: convert each mhtml documents into pdf

note that the module used is only an evaluation copy, the out page will have an
unnatural black background section

'''

import aspose.words as aw
for i in range(1, 127, 1):
    doc = aw.Document("data {}.mhtml".format(i))
    doc.save("Out/Output{}.pdf".format(i))
    print("{} th file complete".format(i))

print("all files completed!")