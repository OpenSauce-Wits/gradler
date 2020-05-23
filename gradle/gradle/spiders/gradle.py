import scrapy


class GradleSpider(scrapy.Spider):
    name = "gradle"
    # This is future will be a database file
    # All you would need to do is
    # Each time there's a new project to mark, you will copy and replace the contents in Software/Tests
    # The start_urls will be a constant
    start_urls = [
        "file:///home/molefe/Software/Tests/com.example.attributechangeproject.ExampleUnitTest.html",
        'file:///home/molefe/Software/Tests/com.example.attributechangeproject.ExampleInstrumentedTest.html'
    ]

    """
    What we can do
    
    1. Lecturer submits only source files
    2. Student submits only source files
    3. Template Project
    4. Build from it
    """

    def fetch_gradle_results(self, tests,results,status):
        test_dir = {}
        test_type = {}
        if len(tests) % 2 == 0:
            # Instrumented Test
            for test in range(len(tests)):
                if test % 2 == 0:
                    test_dir[tests[test]] = tests[test + 1]
            test_type["instrumentation"] = test_dir
        else:
            # Unit Test
            for test in range(len(tests)):
                if test % 2 == 0 and test != len(tests) - 1:
                    test_dir[tests[test]] = tests[test + 2]
            test_type["unit"] = test_dir

        test_type["status"] = self.fetch_status(results,status)
        return test_type

    def fetch_status(self, results, status):
        result_status = {}
        for state, result in zip(status, results):
            result_status[state] = result
        return result_status

    def parse(self, response):
        self.generate_html(response)
        results = response.css('div.infoBox div.counter::text').getall()
        percent = response.css('div.percent::text').get()
        results.insert(0, percent)
        status = ["grade", "tests", "failures", "time"]
        tests = response.css('div#tab0 tr td::text').getall()
        test_type = self.fetch_gradle_results(tests,results,status)
        yield test_type

    def generate_html(self,response):
        package_name = response.url.split("/")[-1]
        test = package_name.split('.')[-2]
        filename = 'gradle-%s.html' % test
        with open(filename,'wb') as f:
            f.write(response.body)
