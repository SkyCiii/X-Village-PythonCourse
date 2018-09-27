import opening
import ending

opening.say()   #雖然都是say function，但是是在不同的module底下，即不同scope，所以不會互相干擾。
ending.say()

