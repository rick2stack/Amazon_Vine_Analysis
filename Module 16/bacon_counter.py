from mrjob.job import MRJob
#this creates a class that uses MRJOb properties
class Bacon_count(MRJob):
    # The mapper will take self a "_" and a line
    #the "_" is just to show a blank value per python standards
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                #yield will "generate" an object, which means
                # it creates a list but isn't store in memory
                #it will only return a value if "next()" is called
                yield "bacon", 1
    # the self is just to represent the instance of the class
    def reducer(self, key, values):
        # this will sum the key values previously yield
        yield key, sum(values)
if __name__ == "__main__":
   Bacon_count.run()
        