$(document).ready(function() {
    $('.game__body-selected').on('change', '.letter__select[type="radio"]', function() {
        var selectedLetter = $(this).val();
        console.log(selectedLetter)
        $.ajax({
            type: 'POST',
            url: '/practice/games/alphabet/',
            data: {
                'letter': selectedLetter,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function(response) {
                var correct = response.correct;
                var newLetters = response.letters;
                // Обработка полученного ответа
                if (correct) {
                    // Вывести блок с надписью "Поздравляю"
                    $('.congratulations').show();
                    // Через 3 секунды отправить GET-запрос для получения нового списка букв
                    setTimeout(function() {
                        $.ajax({
                            type: 'GET',
                            url: '/practice/games/alphabet/',
                            success: function(response) {
                                if (response && response.letters && response.letters.length > 0) {
                                    var letters = response.letters;
                                    var correctLetter = response.correct_letter;
                                    // Обновить список букв
                                    var selectedContainer = $('.game__body-selected');
                                    selectedContainer.empty();
                                    for (var i = 0; i < letters.length; i++) {
                                        var letter = letters[i];
                                        var letterObject = $('<div class="letter__object"></div>');
                                        var letterSelect = $('<input class="letter__select" type="radio" name="letter" value="' + letter + '" required>');
                                        var letterLabelRadio = $('<div class="selected__radio"></div>')
                                        var letterLabel = $('<label for="' + letter + '">' + letter + '</label>');
                                        letterObject.append(letterSelect);
                                        letterObject.append(letterLabelRadio)
                                        letterLabelRadio.append(letterLabel);
                                        selectedContainer.append(letterObject);
                                    }

                                    $('#correctID').text('Выбери букву ' + correctLetter);
                                    // Скрыть блоки поздравления и попробуйте снова
                                    $('.congratulations').hide();
                                    $('.try-again').hide();
                                } else {
                                    console.log('Неверный формат ответа');
                                }
                            },
                            error: function(xhr, status, error) {
                                console.log(error);
                            }
                        });
                    }, 1000);
                } else {
                    // Вывести блок с другой надписью
                    $('.try-again').show();
                }
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        });
    });
});
