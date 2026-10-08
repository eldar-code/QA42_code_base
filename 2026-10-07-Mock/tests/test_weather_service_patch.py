from unittest.mock import Mock, patch
from app import weather_service


@patch("app.weather_service.api.get_weather", return_value={"city": "Eilat", "temp": 41})
def test_get_city_temp(mock_get_weather: Mock):
    # # Arrange
    # mock_get_weather = Mock(return_value={"city": "Eilat", "temp": 41})
    # original_function = weather_service.api.get_weather
    # weather_service.api.get_weather = mock_get_weather
    # Act
    result = weather_service.get_city_temp("Eilat")
    # Assert
    assert result == 41
    mock_get_weather.assert_called_with("Eilat") # find out that the mock was used
    # # Restore
    # weather_service.api.get_weather = original_function
