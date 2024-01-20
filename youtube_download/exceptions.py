class NoStreamsAvailable(Exception):
    def __init__(self, message="No streams are available for download."):
        self.message = message
        super().__init__(self.message)


class NoVideosAvailable(Exception):
    def __init__(self, message="No videos are available for download."):
        self.message = message
        super().__init__(self.message)
