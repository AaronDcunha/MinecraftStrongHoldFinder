# Minecraft Stronghold Finder using Python



This python script would approximately find the coordinates of a stronghold based on two eye of ender throws. Essentially you have to input the coordinates of your first throw along with your angle and do the same after travelling a bit. The script would do simple Line equations and would calculate the coordinates accordingly.
Do note that while the math works, the accuracy is highly dependent on human inputs. To problem with using python and not using a mod is that most of the time we might put a value that is not exactly accurate. This small change is more than enough to cause a large offset. 
I managed to get 2 accurate values and 1 value that was offsetted by 100 blocks. I did get 2 failed values where the coordinates were offsetted by around 1000 blocks.

## How it works
When a player throws an eye of ender, the eye of ender travels towards the direction of where the nearest stronghold is.
So with the help of the first coordinates and the angle, we would find the equation of that line pointing towards the stronghold with the help of the equation : ![Equation of a line](https://wikimedia.org/api/rest_v1/media/math/render/svg/d6756ad5943432d2b4ca4f77734bda1e024a52d7) 
Similarly we would find the equation of the 2nd line from another point by travelling a few blocks in any direction other than towards or coincident with the first line.
The equations are then solved for **x** and **z** (The Y Coordinate does not matter).
The coordinates (x , ~ , z) would approximately be the coordinates of the stronghold.
![Diagram](https://i.ibb.co/vmTXPpX/Untitled.png)
![Pearl 1](https://i.ibb.co/5LkXL9m/image.png)

## Problems I face
- Since it is based on human input, there are extreme chances of errors which could lead to wrong coordinates as the final answer. The math is correct but it is a bit difficult to be really accurate especially with the angles. As small changes could eventually lead to major offsets.
- The solution? A mod which would grab an even more accurate information and accordingly calculate the coordinates.
- Another source of error is going in a direction where the enderpearl would then face towards another stronghold.
- Possibly a source of error is just going towards the line that heads towards the stronghold which is basically the same as line 1.


Feel free to make a mod using this concept. I am pretty sure I heard of this concept somewhere else instead of making it up by myself. I do not exactly remember where I heard the concept before but I came up with this random idea and decided to calculate it via python. Mostly because I did not learn how to make minecraft mods yet.

