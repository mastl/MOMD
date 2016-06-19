# My Own Markdown
18-06-2016

The title is in the first line. If not specified otherwise, it will be a heading 1.

## Headings
Headings follow markdown.

Heading 1: #
Heading 2: ##
Heading 3: ###
Heading 4: ####
Heading 5: #####
Heading 6: ######

Headings must be declared at the start of a line. 

## Comments
%% Comments that will not be displayed when published are started with "%%". They must be at the start of a line.


## Lists
Initialize a unordered list that displays bullets with "+". 
Initialize ordered list by "i.", "1.", "a." or "A.". All following the first should just be "+".


## Tagging classes
It is possible create usergenerated classes (like for example "post" if one is writing a blog) by writing "<class_name>". These classes are used for formating purposes 

## Tagging elements
Elements in the file (like for example the section on lists above) can be tagged by "<<element_name>>". By default everthing following an element statement will belong to that element until a new element statement is made. Note, though, that headings and subsequent text are considered to be elements.

It is possible to make statements about which elements belong to which classes. I.e. it will in practice only be necessary to define elements and then make statements like: element_1, element_2, element_3 --> class_1