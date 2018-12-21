# -*- encoding:utf-8 -*-
import sys
import csv


def set_difference(twolist):
    set1 = set()
    set2 = set()
    twolist1 = twolist[0]
    twolist2 = twolist[1]
    for i in twolist1:
        set1.add(tuple(i))
    for i in twolist2:
        set2.add(tuple(i))
    # mysql中有，我解析的里面没有
    # print(set1.difference(set2))
    # mysql中没有，我解析的里面有
    # print(set2.difference(set1))
    # 两个堆的交集
    # print(set1.intersection(set2))
    # 两个堆的并集
    # print(set1.union(set2))

    return set1.difference(set2), set2.difference(set1), set1.intersection(set2), set1.union(set2)


def store_in_csv(set1, set2, set3, set4):

    with open('.result.csv', 'w') as fcsv:
        fcsv.write(
            'carr,fltNo,bkClass,departureTime,arrivalTime,departureAirport,arrivalAirport,codeshare,passengerType,yFareAmount,disAmt\n')
        fcsv.write("mysql中有但我解析的里面没有\n")
        for i1 in set1:
            fcsv.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}\n'.format(
                i1[0], i1[1], i1[2], i1[3], i1[4], i1[5], i1[6], i1[7], i1[8], i1[9], i1[10]))
        fcsv.write("mysql中没有但我解析的里面有\n")
        for i1 in set2:
            fcsv.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}\n'.format(
                i1[0], i1[1], i1[2], i1[3], i1[4], i1[5], i1[6], i1[7], i1[8], i1[9], i1[10]))

        fcsv.write("两个堆的交集\n")
        for i1 in set3:
            fcsv.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}\n'.format(
                i1[0], i1[1], i1[2], i1[3], i1[4], i1[5], i1[6], i1[7], i1[8], i1[9], i1[10]))

        fcsv.write("两个堆的并集\n")
        for i1 in set4:
            fcsv.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}\n'.format(
                i1[0], i1[1], i1[2], i1[3], i1[4], i1[5], i1[6], i1[7], i1[8], i1[9], i1[10]))


def clean_list(twolist):
    for l in twolist:
        l.pop(0)
        for i in l:
            i.pop(3)
            i.pop(4)
            if i[7] == 'None':
                i[7] = ''
            i[9] = float(i[9])
            i[10] = float(i[10])
            if i[1] == '4945':
                print(i)
    return twolist


def main(argv):
    info_temp = list()
    for jsonfile in argv:
        # print(jsonfile)
        data = []
        with open('.'+jsonfile, 'r') as csv_file:
            csv_reader_lines = csv.reader(csv_file)
            for line in csv_reader_lines:
                data.append(line)
                # print(line)

        info_temp.append(data)
    set1, set2, set3, set4 = set_difference(clean_list(info_temp))
    store_in_csv(set1, set2, set3, set4)

    print("done!")


if __name__ == "__main__":
    main(sys.argv[1:])
