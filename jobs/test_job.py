from job_scheduler.job import Job

class TestJob(Job):
    """
        Test Job
        You write a job to do just anything you want, while making sure your API does not break.
    """

    def process(self, **kwargs):
        name = kwargs["name"]
        print(f"Hello {name}!")
        # ADD SUCCESS ALERT HERE
        return True