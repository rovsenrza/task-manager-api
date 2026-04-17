# Nəticə

## Layihəyə Ümumi Baxış

**Task Manager API** — Python və Flask texnologiyaları əsasında hazırlanmış, istehsala hazır REST API-dir. Layihə, tapşırıqların idarə edilməsi üçün tam funksional bir veb xidməti təqdim edir.

## Həyata Keçirilənlər

### API Endpointləri
Layihə çərçivəsində aşağıdakı endpointlər tətbiq edilmişdir:

| Endpoint | Metod | Təsvir |
|---|---|---|
| `/health` | GET | Servisin sağlamlıq yoxlaması |
| `/info` | GET | Tətbiq versiyası və konfiqurasiya |
| `/tasks` | GET | Bütün tapşırıqların siyahısı |
| `/tasks` | POST | Yeni tapşırıq yaratmaq |
| `/tasks/<id>` | GET | Müəyyən tapşırığı əldə etmək |
| `/tasks/<id>` | PATCH | Tapşırığı tamamlanmış/tamamlanmamış kimi işarələmək |
| `/tasks/<id>` | DELETE | Tapşırığı silmək |

### Texniki Komponentlər

- **Flask Blueprint** arxitekturası ilə modulyar kod strukturu
- **In-memory data saxlama** — sürətli prototipləmə üçün uyğun yanaşma
- **Mühit dəyişənləri** (`APP_VERSION`, `MAX_TASKS`, `PORT`) vasitəsilə çevik konfiqurasiya
- **Docker** dəstəyi ilə konteynerləşdirmə
- **GitHub Actions** ilə avtomatik CI pipeline
- **pytest** ilə unit testlər
- **flake8** ilə kod keyfiyyəti yoxlaması

## Öyrənilənlər

Bu layihə aşağıdakı bilik və bacarıqları inkişaf etdirdi:

1. **REST API dizaynı** — HTTP metodları, status kodları və resursoriyentirli arxitektura
2. **DevOps təcrübələri** — CI/CD pipeline, Docker ilə konteynerləşdirmə
3. **Git iş axını** — feature branch-dan main-ə PR vasitəsilə birləşdirmə, versiya teqləmə (`v1.0.0`)
4. **Kod keyfiyyəti** — linter inteqrasiyası və avtomatik testlər
5. **Konfiqurasiya idarəetməsi** — sirləri kodda saxlamamaq, `.env` istifadəsi

## Nəticə

Task Manager API layihəsi müasir veb xidmət inkişafının əsas prinsiplərini uğurla nümayiş etdirir. Layihə sadə, lakin genişlənə bilən bir arxitektura əsasında qurulmuş, DevOps ən yaxşı təcrübələrini özündə birləşdirən tam bir həll kimi tamamlanmışdır.

Gələcəkdə bu layihəni inkişaf etdirmək üçün verilənlər bazası inteqrasiyası (PostgreSQL və ya SQLite), JWT əsaslı autentifikasiya və genişləndirilmiş sənədləşmə (Swagger/OpenAPI) əlavə edilə bilər.
