from aiogram.types import FSInputFile
from qrcode.main import QRCode
import qrcode




def create_qr_cod(file_name:str, url: str = "https://meet.google.com/gqk-ijpg-tqa") -> dict[str, str | FSInputFile]:
    '''

    :param file_name: Название файла
    :param url: Ссылки тестовая
    :return: {
        'file': file_name,
        'fsi': FSInputFile(file_name)
    }
    '''
    # Создаем объект QRCode
    qr = QRCode(
        version=1,  # Размер QR-кода (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Уровень коррекции ошибок
        box_size=10,  # Размер "пикселей" QR-кода
        border=4,  # Размер белой рамки (в блоках)
    )

    # Добавляем данные
    qr.add_data(url)
    qr.make(fit=True)

    # Создаем изображение
    img = qr.make_image(fill_color="black", back_color="white")
    if file_name.endswith('.png') is False:
        file_name = file_name + '.png'

    # Сохраняем
    img.save(f"{file_name}")
    dct = {
        'file': file_name,
        'fsi': FSInputFile(file_name)
    }
    return dct

