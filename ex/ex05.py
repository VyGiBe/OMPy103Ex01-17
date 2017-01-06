# -*- coding: utf-8 -*-


# Exercise 05

my_name = 'Jian Wang'
my_age = 23 # not a lie
my_height = 173 # centimeter
my_weight = 68 # kilogram
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually, that's not too heavy."
print "He's got a %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth


# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)



# Study Drills

name = 'Jian Wang'
age = 23 # I was born in 1993.
height_cm = 173 # cm
weight_kg = 68 # kg
weight_lbs = round( 2.2046 * weight_kg ) # lbs
height_inches = round( 0.3937 * height_cm ) # inch
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d cm tall." % height_cm
print "Or he's %d inches tall." % height_inches
print "He's %d kg heavy." % weight_kg
print "Or he's %d lbs heavy." % weight_lbs
print "Actually, that's not too heavy."
print "He's got a %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth


# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
	age, height_cm, weight_kg, age + height_cm + weight_kg)
	