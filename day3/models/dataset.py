from dataclasses import dataclass


@dataclass
class Dataset(object):
    context: str
    fname: str
    train: object
    test: object
    id: str
    label: str

    # getter
    @property
    def context(self) -> str: return self._context

    # setter
    @context.setter
    def context(self, context): self._context = context

    # getter
    @property
    def fname(self) -> str: return self._fname

    # setter
    @fname.setter
    def fname(self, fname): self._fname = fname

    # getter
    @property
    def train(self) -> object: return self._train

    # setter
    @train.setter
    def train(self, train): self._train = train

    # getter
    @property
    def test(self) -> object: return self._test

    # setter
    @test.setter
    def test(self, test): self._test = test

    # getter
    @property
    def id(self) -> str: return self._id

    # setter
    @id.setter
    def id(self, id): self._id = id

    # getter
    @property
    def label(self) -> str: return self._label

    # setter
    @label.setter
    def label(self, label): self._label = label

