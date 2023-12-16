# An Introduction to Game Development in Python and Godot - with Christian Koch

I am learning how Python and Godot can be utilized together for making games. This is my first round at coding something substantial.

## VLOG

### June 2023
1. Intermittent dev times led me to stop at 20.Meteor Dodger 3 - Spaceship Movement. Had troubles with curser still being visible. Need to stop as main job is picking up in amount of work

### December 2023
1. Started coding again. Worked on adding laser spawing from the ship on click. This was taught in 22.Meteor Dodge 6 - Creating a laser. Still had issues with cursor displaying an not being hidden.

2. Reorganized the groups at the end of the file to draw the groups on the correct layers. Since all is drawn on top in order of appearence, this made the laser more beleivable that it was coming from a gun mounted underneath the spacecraft.

3. 4:03pm - Found the method on Python-CE Docs. https://pyga.me/docs/ref/mouse.html#pygame.mouse.set_visible. 
```python
pygame.mouse.set_visible()
```

4. Since I already defined the class SpaceShip, I placed the new code in the def update as below. This created the desired change.
```python
pygame.mouse.set_visible(False)
```

5. Added killswitch for laser after leaving the active window to midigate frame data.
```python
if self.rect.centery <-50:
self.kill()
```