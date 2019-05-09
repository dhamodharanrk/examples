__author__ = 'dhamodharan.k'
import csv

class pagination_tutorial:

    # We defined as function since it will write header each time. to avoid it its a simple tweaking
    header_added = False

    # Here each time file opened with append mode and write each row(pages data.)
    def write_file(self, content):
        with open('output.csv', 'a', newline='') as csvfile:
            writer_ptr = csv.DictWriter(csvfile, delimiter='\t',fieldnames=['Upplagtdatum', 'Titel','Stad Kommun'])
            if not self.header_added:
                writer_ptr.writeheader()
                self.header_added = True
            writer_ptr.writerow(content) # Here am using write row you can also use list of rows
            # writer_ptr.writerows(pages_data) # It will write list of dicts

    def do_save(self,rows):
        self.write_file(rows)

if __name__ == '__main__':
    obj = pagination_tutorial()
    # Consider this as data (Each row is each page)
    pages_data = [{'Upplagtdatum': ['Yes'], 'Titel': ['a'], 'Stad Kommun': ['ab']},
            {'Upplagtdatum': ['No'], 'Titel': ['b'], 'Stad Kommun': ['abc']},
            {'Upplagtdatum': ['NA'], 'Titel': ['c'], 'Stad Kommun': ['abcd']},
            {'Upplagtdatum': ['No'], 'Titel': ['d'], 'Stad Kommun': ['abcde']}]
    for pages in pages_data:
        obj.do_save(pages)
