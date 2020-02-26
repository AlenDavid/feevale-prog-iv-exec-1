# 	1. Create a connection with "database.txt"
# 	(There's an exercise where we have to use some find algorithm,
# 	so will be great to have something prepared for that too)
#	2. Create an interpreter for names and ages
#	3. We need to use a functional archetype
# 	for this project (It should be easy this way)

from math import ceil


def nametest(a, b):
    for i in range(0, a.__len__()):
        if a[i] != b[i]:
            return -1 if ord(a[i]) < ord(b[i]) else 1

    return 0


class DatabaseConnection(object):

    def get(self, numrow):
        self.open()
        offset = self.seek_file_offset(numrow)

        self.file.seek(offset)

        line = self.file.readline()

        self.close()
        return line

    def seek_file_offset(self, numrow):
        if numrow >= self.database_rows_count:
            return -1

        self.file.seek(0)
        i = 0

        if numrow == 0:
            return 0

        while i != numrow:
            a = self.file.read(1)
            if a == '\n':
                i += 1

        return self.file.tell()

    def get_all(self):
        self.open()
        # rows = self.file.read().split('\n')

        people = []

        for row in self.file:
            columns = row.split('#')
            name = columns[0]
            age = columns[1]

            people.append({'name': name, 'age': age})
            pass

        self.close()
        return (people)

    def get_name_brute_force_search(self, ref):  # exec 2_1
        self.open()
        iterations = 0

        for row in self.file:
            name = str(row.split('#')[0])
            iterations += 1

            if name == ref:
                return (iterations)

        self.close()
        return (iterations)

    def get_name_binary_search(self, ref):  # exec 2_2
        self.open()
        iterations = 1

        move = 0
        mark_min = 0
        mark_max = self.database_rows_count

        marker = mark_min + int(ceil((mark_max - mark_min) / 2))

        while marker != mark_max and marker != mark_max:
            marker = mark_min + int(ceil((mark_max - mark_min) / 2))

            row = self.get(marker)
            name = row.split('#')[0]

            move = nametest(ref, name)

            if move == 0:
                break
            if move == -1:
                mark_max = marker
            if move == 1:
                mark_min = marker

            iterations += 1

        self.close()
        return (iterations)

    def open(self):
        self.file = open(self.file_path, 'r')

        count = 0
        for line in self.file.xreadlines():
            count += 1

        self.database_rows_count = count

        self.file.seek(0)

    def close(self):
        self.file.close()

    def __init__(self, path):
        try:
            self.file_path = path
            self.open()
        except:
            self = None


def calc_average_age(people):  # exec 1_1
    ages = 0
    i = 0
    for person in people:
        i += 1
        ages += float(person.get('age'))

    return (ages / i)


def calc_rec_first_name(people):  # exec 1_2
    rec_names = {}
    most_rec_name = ''
    most_rec_names = ''

    for person in people:
        name = person.get('name')
        first_name = name.split(' ')[0]

        if not rec_names.has_key(first_name):
            rec_names[first_name] = 1
        else:
            rec_names[first_name] += 1
        pass

    for name in rec_names:
        if most_rec_name is '':
            most_rec_name = name

        if rec_names[name] > rec_names[most_rec_name]:
            most_rec_names = ''
            most_rec_name = name
            most_rec_names = most_rec_names

        elif rec_names[name] is rec_names[most_rec_name]:
            most_rec_names += ' ' + most_rec_name

    return (most_rec_name)


def calc_first_name_quant(people):  # exec 1_3
    names = {}

    for person in people:
        name = person.get('name')
        first_name = name.split(' ')[0]

        if not names.has_key(first_name):
            names[first_name] = 1
        else:
            names[first_name] += 1
        pass

    return (names)


if __name__ == "__main__":
    database_path = './database.txt'
    conn = DatabaseConnection(database_path)

    all_people = conn.get_all()

    # first exercise list

    # exec_1_1 = calc_average_age(all_people)
    # exec_1_2 = calc_rec_first_name(all_people)
    # exec_1_3 = calc_first_name_quant(all_people)

    # # uncomment for testing
    # # print(exec_1_1)
    # # print(exec_1_2)
    # # print(exec_1_3)

    # second exercise list

    # search_name = 'Insert some name'

    # exec_2_1 = conn.get_name_brute_force_search(search_name)
    # exec_2_2 = conn.get_name_binary_search(search_name)

    # # uncomment for testing
    # # print(exec_2_1)
    # # print(exec_2_2)

# end
