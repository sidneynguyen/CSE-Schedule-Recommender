# CSE Schedule Recommender

A program that can recommend a schedule for the year for CSE students.

Ideas

Get prereq data
https://cse.ucsd.edu/undergraduate/courses/prerequisites-cse-undergraduate-classes

Get course offerings
http://cse.ucsd.edu/undergraduate/courses/2017-2018-tentative-undergraduate-course-offerings

The idea is to use data provided by the user (what courses they've taken) and data scraped from the
websites (prereqs/offerings) to recommend which courses to take for the quarter.

User will provide:
courses taken
number of courses wanted per quarter
number of GEs wanted to take during the year

Basic algorithm:
choose courses iteratively and based on prereqs

Future plans:
recommend based on cape reviews