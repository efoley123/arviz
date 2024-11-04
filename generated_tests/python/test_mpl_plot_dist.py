import pytest
from unittest.mock import patch
from your_module_name import plot_distributions  # Adjust the import according to your file structure

@pytest.fixture
def mock_plt_show():
    with patch('matplotlib.pyplot.show') as mock_show:
        yield mock_show

@pytest.fixture
def mock_az_style():
    with patch('arviz.style.use') as mock_style:
        yield mock_style

@pytest.fixture
def mock_np_random_poisson():
    with patch('numpy.random.poisson') as mock_random_poisson:
        yield mock_random_poisson

@pytest.fixture
def mock_np_random_normal():
    with patch('numpy.random.normal') as mock_random_normal:
        yield mock_random_normal

@pytest.fixture
def mock_az_plot_dist():
    with patch('arviz.plot_dist') as mock_plot_dist:
        yield mock_plot_dist

def test_plot_distributions_calls_style_use(mock_az_style):
    """Ensure arviz style is applied."""
    plot_distributions()
    mock_az_style.assert_called_with("arviz-doc")

def test_plot_distributions_generates_correct_random_data(mock_np_random_poisson, mock_np_random_normal):
    """Check if the correct random data is generated for both distributions."""
    plot_distributions()
    mock_np_random_poisson.assert_called_with(4, 1000)
    mock_np_random_normal.assert_called_with(0, 1, 1000)

def test_plot_distributions_creates_correct_subplots():
    """Verify if the subplots are correctly created with appropriate titles."""
    fig, ax = plot_distributions()
    assert ax[0].get_title() == "Poisson"
    assert ax[1].get_title() == "Gaussian"

def test_plot_distributions_calls_plot_dist_correctly(mock_az_plot_dist):
    """Ensure arviz's plot_dist is called with correct parameters for both distributions."""
    plot_distributions()
    calls = [call for call in mock_az_plot_dist.call_args_list]
    assert calls[0][1]['label'] == "Poisson"
    assert calls[1][1]['label'] == "Gaussian"

def test_plot_distributions_shows_plot(mock_plt_show):
    """Test if the plot display function is called."""
    plot_distributions()
    mock_plt_show.assert_called_once()