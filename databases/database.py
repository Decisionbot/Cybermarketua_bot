import time

import aiosqlite


class MyDb:
    __dbname__ = "databases/cooldown_timer.db"

    async def bd_start(self):
        async with aiosqlite.connect(self.__dbname__) as db:
            async with db.cursor() as cursor:
                if db:
                    await cursor.execute("CREATE TABLE if NOT EXISTS timer_db(user_id INTEGER PRIMARY KEY UNIQUE NOT "
                                         "NULL, "
                                         "cooldown_timer INTEGER, photo_1 TEXT, photo_2 TEXT, photo_3 TEXT,  "
                                         "photo_4 TEXT, photo_5 TEXT photo_6 TEXT, photo_7 TEXT, photo_8 TEXT,  "
                                         "photo_9 TEXT, photo_10 TEXT)")
                    await db.commit()

    async def sql_create_time(self, user_id):
        async with aiosqlite.connect(self.__dbname__) as db:
            if await self.get_user(user_id) is None:
                await db.execute("INSERT INTO timer_db (user_id) VALUES(?)", (user_id,))
                await db.commit()

    async def sql_update_time(self, cooldown_timer, user_id):
        async with aiosqlite.connect(self.__dbname__) as db:
            await db.execute("UPDATE timer_db SET cooldown_timer = ? WHERE user_id = ?", (int(cooldown_timer),
                                                                                          user_id,))

            await db.commit()

    async def sql_update_photo(self, column, photo_file, user_id):
        async with aiosqlite.connect(self.__dbname__) as db:
            await db.execute(f"UPDATE timer_db SET photo_{column} = ? WHERE user_id = ?", (photo_file,
                                                                                           user_id))

            await db.commit()

    async def get_user(self, user_id):
        async with aiosqlite.connect(self.__dbname__) as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT * FROM timer_db WHERE user_id = ?", (user_id,))

                return await cursor.fetchone()

    async def get_time(self, user_id):
        async with aiosqlite.connect(self.__dbname__) as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT cooldown_timer FROM timer_db WHERE user_id = ?", (user_id,))
                user = await cursor.fetchone()
                return int(int(time.time()) - int(user[0]))

    async def get_photos(self, user_id):
        async with aiosqlite.connect(self.__dbname__) as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT photo_1, photo_2, photo_3, photo_4, photo_5, photo_6, photo_7, photo_8, "
                                     "photo_9, photo_10 FROM timer_db WHERE "
                                     "user_id = ?", (user_id,))
                photos = await cursor.fetchone()
                return photos
