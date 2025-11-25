# # lessons=['backend','frontend','ciber','dizayn','smm'] # 20000 searching
# # lesson_tuple=('backend','frontend','ciber','dizayn','smm')
# # lessons.append('target')
# # lesson_tuple=list(lesson_tuple)
# # lesson_tuple.append('new')
# # lesson_tuple=tuple(lesson_tuple)
# # # lesson_tuple='salom'
# # print(lesson_tuple)
# # # lesson_tuple.append('new')
# # # print(lesson_tuple)
# # # print(lessons)
# # from linecache import updatecache
# #
# # # tuple ichidagi elementni oqish(read)
# # my_tuple=(10,20,30)4
# # print(my_tuple[0])
# #
# # # bo'laklash(slicing);'
# # my_tuple=(10,20,30)
# # print(my_tuple[1:3])
# #
# #
# # # tule yangilash (updatecache)
# # old_tuple=(1,2,3)
# # new_tuple=old_tuple+(4,5)
# # print(new_tuple)
# #
# # students = ("Ali",  "Zebo", "Javohir", "Ali", "Zebo", "Ali")
# # print(students.count("Zebo"))
# # print(students.count("Ali"))
# # scores = (85, 90, 78, 92, 88)
# # print(sorted(scores))
#
#      # set malumotlar turi
# # new_set={'non','choy','non',True,1,0}
# # print(new_set)
# #     element qoshish
# # fruist={'olma','nok'}
# # fruist.add("olma")
# # print(fruist)
# # # element o'chirish'
# # fruist.remove("olma")
# # fruist.discard('non')
# # print(fruist)
# # # setni tozalash
# # fruist.clear()
# # print(fruist)
# # del fruist
#
#
# #
# # # birlashtirish
# # #  .union() kodi
# # a={1,2,3}
# # b={3,4,5,}
# # print(a.union(b))
# #
# # # kesishma(intersectin)
# # # ikkita setni ummumiy elementini olish:
# # a={1,2,3}
# # b={2,3,4}
# # print(a.intersection(b))
# #
# # # Farq(difference) birinchi setdagi,lekin ikkinchi setda yoq elementlarni olish:
# # a={1,2,3}
# # b={2,3,4}
# # print(a.difference(b))
# #
# # # simmetrik farq(symmetric_difference) ikkala setning faqat ummumiy bo'lmagan elementlarini olish'
# # a={1,2,3}
# # b={2,3,4}
# # print(a.symmetric_difference(b))
# #
# #
# #
#
#
# # math_students={"ali","zebo","said"}
# # english_students={"said","javohir","ali"}
# # print(math_students.intersection(english_students))
#
#
#
# #   homework
#
# # 1
nums = {1, 2, 3, 2, 4, 1, 5}
print(tuple(nums))
# #
# # 2
a ={1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.intersection(b))
# 3
a = {1, 2, 3, 4}
b = {3, 4, 5 ,6}
print(a.difference(b))
#  4
son = [1, 2, 2, 3, 4, 4, 5]
a=set(son)
print(len(a))
#  5
