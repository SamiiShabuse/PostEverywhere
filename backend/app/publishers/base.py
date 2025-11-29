from abc import ABC, abstractmethod


class Publisher(ABC):
    """Abstract publisher interface. Implement platform-specific adapters."""

    @abstractmethod
    def publish(self, file_path: str, title: str, **kwargs):
        """Publish a video file. Returns a dict with status/info."""
        raise NotImplementedError()
