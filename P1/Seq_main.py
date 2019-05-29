#Exercise I part II lesson P1

from P1.Seq import Seq

Sequence1 = Seq("ACTGAATTCTTGC")
Sequence2 = Seq("CCTGA")
Sequence3 = Seq.compl(Sequence1)
Sequence4 = Seq.rev(Sequence3)


print("1º Sequence: {}".format(Sequence1))
print("Length for 1º Sequence: {}".format(Seq.len(Sequence1)))
print("Bases count for 1º Sequence: A:{}, C:{}, T:{}, G:{}".format(Sequence1.Count("A"), Sequence1.Count("C"), Sequence1.Count("T"), Sequence1.Count("G")))
print("Bases percentage for 1º Sequence: A:{}, C:{}, T:{}, G:{}".format(Sequence1.percent("A"), Sequence1.percent("C"), Sequence1.percent("T"), Sequence1.percent("G")))


print("2º Sequence: {}".format(Sequence2))
print("Length for 2º Sequence: {}".format(Seq.len(Sequence2)))
print("Bases count: A:{}, C:{}, T:{}, G:{}".format(Sequence2.Count("A"), Sequence2.Count("C"), Sequence2.Count("T"), Sequence2.Count("G")))
print("Bases percentage: A:{}, C:{}, T:{}, G:{}".format(Sequence2.percent("A"), Sequence2.percent("C"), Sequence2.percent("T"), Sequence2.percent("G")))


print("Third Sequence is: {}".format(Sequence3))
print("Length is: {}".format(Seq.len(Sequence3)))
print("Bases count: A:{}, C:{}, T:{}, G:{}".format(Sequence3.Count("A"), Sequence3.Count("C"), Sequence3.Count("T"), Sequence3.Count("G")))
print("Bases percentage: A:{}, C:{}, T:{}, G:{}".format(Sequence3.percent("A"), Sequence3.percent("C"), Sequence3.percent("T"), Sequence3.percent("G")))


print("Fourth Sequence is: {}".format(Sequence4))
print("Length is: {}".format(Seq.len(Sequence4)))
print("Bases count: A:{}, C:{}, T:{}, G:{}".format(Sequence4.Count("A"), Sequence4.Count("C"), Sequence4.Count("T"), Sequence4.Count("G")))
print("Bases percentage: A:{}, C:{}, T:{}, G:{}".format(Sequence4.percent("A"), Sequence4.percent("C"), Sequence4.percent("T"), Sequence4.percent("G")))