#  git config --global user.name "Your Name"
# git config - -global user.email "your_email@whatever.com"


# git add hello.html
# git commit - m "Initial Commit" Теперь давайте добавим в репозиторий
# \

# Используйте команду git status, чтобы проверить текущее состояние репозитория.

# Выполните
# git status



# git add a.html
# git add b.html
# git commit -m "Changes for a and b"



# $ git status
# On branch main
# nothing to commit, working tree clean



# $ git add .
# $ git status
# On branch main
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
# 	modified:   hello.html



# Получение списка произведенных изменений — функция команды git log.

# Выполните
# git log



# Однострочная история
# Вы полностью контролируете то, что отображает log. Мне, например, нравится однострочный формат:

# Выполните
# git log --pretty=oneline



# Выполните
# git log
# Результат
# $ git log
# b7614c1 2023-11-28 | Added HTML header (HEAD -> main) [Alexander Shvets]
# 46afaff 2023-11-28 | Added standard HTML page tags [Alexander Shvets]
# 78433de 2023-11-28 | Added h1 tag [Alexander Shvets]
# 5836970 2023-11-28 | Initial commit [Alexander Shvets]
# Просмотрите историю изменений и найдите хеш первого коммита. Он должен быть в последней строке результата git log. Используйте этот хеш (достаточно первых 7 символов) в команде ниже. Затем проверьте содержимое файла hello.html.

# Выполните
# git checkout <hash>
# cat hello.html
# Многие команды Git принимают хеши коммитов в качестве аргументов. Хеши коммитов будут отличаться в разных репозиториях, поэтому когда вы видите, что в команде есть пометка <hash>, то это значит, что вам надо подставить вместо нее реальный хеш из вашего репозитория.

# Вы увидите:

# Результат
# $ git checkout 5836970
# Note: switching to '5836970'



# Командаswitch является одной из них —
# ее единственным назначением является переключение между ветками. Команда checkout все еще доступна, но использовать 
# ее для переключения веток больше не рекомендуется.


# Давайте назовем текущую версию страницы hello.html первой, то есть v1.

# 01Создайте тег первой версии
# Выполните
# git tag v1
# git log
# Результат
# $ git tag v1
# $ git log
# b7614c1 2023-11-28 | Added HTML header (HEAD -> main, tag: v1) [Alexander Shvets]
# 46afaff 2023-11-28 | Added standard HTML page tags [Alexander Shvets]
# 78433de 2023-11-28 | Added h1 tag [Alexander Shvets]
# 5836970 2023-11-28 | Initial commit [Alexander Shvets]


# Выполните
# git tag v1-beta
# git log
# Результат
# $ git tag v1-beta
# $ git log
# 46afaff 2023-11-28 | Added standard HTML page tags (HEAD, tag: v1-beta) [Alexander Shvets]
# 78433de 2023-11-28 | Added h1 tag [Alexander Shvets]
# 5836970 2023-11-28 | Initial commit [Alexander Shvets]



# Переключение по имени тега
# Теперь попробуйте попереключаться между двумя отмеченными версиями.

# Выполните
# git checkout v1
# git checkout v1-beta
# Результат
# $ git checkout v1
# Previous HEAD position was 46afaff Added standard HTML page tags
# HEAD is now at b7614c1 Added HTML header
# $ git checkout v1-beta
# Previous HEAD position was b7614c1 Added HTML header
# HEAD is now at 46afaff Added standard HTML page tags



# Просмотр тегов с помощью команды tag
# Вы можете увидеть, какие теги доступны, используя команду git tag.

# Выполните
# git tag
# Результат
# $ git tag
# v1
# v1-beta

# Отмена изменений в рабочем каталоге
# Используйте команду checkout для переключения в версию файла hello.html в репозитории.

# Выполните
# git checkout hello.html
# git status
# cat hello.html


# Сбросьте области подготовки
# Команда reset сбрасывает область подготовки к HEAD. Это очищает область подготовки от изменений, которые мы только что проиндексировали.

# Выполните
# git reset HEAD hello.html
# Результат
# $ git reset HEAD hello.html
# Unstaged changes after reset:
# M	hello.html
# Команда reset (по умолчанию) не изменяет рабочую директорию.
# Поэтому рабочая директория всё еще содержит нежелательный комментарий. Мы можем использовать команду checkout из предыдущего урока, 
# чтобы убрать нежелательные изменения в рабочей директори