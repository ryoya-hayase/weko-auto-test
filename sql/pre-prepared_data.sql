-- ユーザー
INSERT INTO accounts_user(email, password, active)
VALUES
    ('repoadmin@weko-selenium.jp', '$pbkdf2-sha512$25000$EmJsDcG4V6rV.p9TqhWilA$qa0zUFXuGHE0ZGn/TCu3dMXcJe7UyN2Ev1cnUcqzxlIBP3DkL0CUxW.FwzD/SUBho1zmJP/z9U3M2/.C7NeQxA', True),
    ('comadmin@weko-selenium.jp', '$pbkdf2-sha512$25000$rVWqdU4pJeScEyIkJCQEQA$a2sKIHadMADTBmHpItCbhBkH18zMuvEypV0V0MEDnOOMjGQVLdaIPy3XN1v6pPmxHxoIQer5CF8wLyYJXpULkg', True),
    ('reg-contributor@weko-selenium.jp', '$pbkdf2-sha512$25000$fa.VkpLSGqNUipESwnivNQ$/lNZdgSONz.uKOrvTTegfZ9dpCEy8nXOwYaG48xYUbM2o/LFO3JU3uel8CGDVlcIRTHW8IppNIG27Bw0OKJPMQ', True),
    ('noreg-contributor@weko-selenium.jp', '$pbkdf2-sha512$25000$VKqVcu4dI2QsBSDkvJdyLg$b.LYu6VL.6uNeri9FXYaHl9AJkeVXl5lUTYuvM2laNIFmi6oqqwzUkZqxRwWNAhR.MiDCsuWymZWwbFNAoE5kw', True),
    ('prxreg-contributor@weko-selenium.jp', '$pbkdf2-sha512$25000$Rah1jlFKyXnv3bv3PsdYCw$vXZKR.qbsvYQL2kMDQyqFiosag8RpK.62IWuDfXuuxhEbG1LAWNM78AQ.TC38Ne7ytxS5XvGAjDRm1QYElW1Wg', True),
    ('general@weko-selenium.jp', '$pbkdf2-sha512$25000$KwXAGOPcuxeiFOI8xxhDqA$YFjpseBU2AYJpajs0yB2MoFZBq9fIdIzoZGO69miHCsdwVKUYOPnVE.3bmJ2WJHraI.LJcIX4jNiI8We7gSMsA', True),
    ('sysadmin@weko-selenium.jp', '$pbkdf2-sha512$25000$HQNASIlRyrl3jjGmlDLG2A$XC5AgpHaJCCTFeffAs93NG/6/RJ0gh6B.57jYXs6kHZVBERlzt9J8qAaCnU7YqSlGFN1LshEgurC1RWvV.TEgQ', True);

-- ユーザーロール
INSERT INTO accounts_userrole(user_id, role_id)
SELECT user_id, role_id
FROM (
    SELECT au.id user_id, au.email email, ar.id role_id, ar.name role_name
    FROM accounts_user au
    CROSS JOIN accounts_role ar
) sub
WHERE (email = 'repoadmin@weko-selenium.jp' AND role_name = 'Repository Administrator')
    OR (email = 'comadmin@weko-selenium.jp' AND role_name = 'Community Administrator')
    OR (email IN ('reg-contributor@weko-selenium.jp', 'noreg-contributor@weko-selenium.jp', 'prxreg-contributor@weko-selenium.jp') 
        AND role_name = 'Contributor')
    OR (email = 'general@weko-selenium.jp' AND role_name = 'General')
    OR (email = 'sysadmin@weko-selenium.jp' AND role_name = 'System Administrator');

-- インデックス
INSERT INTO index
VALUES
    (TIMESTAMP '2024-06-14 08:18:35.300',TIMESTAMP '2024-06-14 08:18:48.821',1718353115275,0,-98,'シークレットURL','Secret URL','','New Index','',False,'',False,5,True,'1','',True,null,False,False,False,False,'3,4,5,-98,-99',False,'3,4,5,-98,-99',False,'',False,'',False,1,'{}',False,'','','',False),
    (TIMESTAMP '2024-06-17 00:22:27.616',TIMESTAMP '2024-06-17 00:24:36.977',1718583747245,0,-97,'利用申請テスト','Usage Application Test','','New Index','',False,'',False,5,True,'1','',True,null,False,False,False,False,'3,4,5,-98,-99',False,'3,4,5,-98,-99',False,'',False,'',False,1,'{}',False,'','','',False);

-- メールテンプレート
INSERT INTO public.mail_templates(mail_subject, mail_body, default_mail, genre_id)
SELECT CONCAT('テスト_', mail_subject), mail_body, default_mail, genre_id FROM (SELECT * FROM public.mail_templates WHERE genre_id = 1 LIMIT 1) sub
UNION ALL
SELECT CONCAT('テスト_', mail_subject), mail_body, default_mail, genre_id FROM (SELECT * FROM public.mail_templates WHERE genre_id = 2 LIMIT 1) sub
UNION ALL
SELECT CONCAT('テスト_', mail_subject), mail_body, default_mail, genre_id FROM (SELECT * FROM public.mail_templates WHERE genre_id = 3 LIMIT 1) sub;

-- 利用規約
-- 更新件数が0件の場合、制限公開用の設定を何かしら編集し、レコードを作成してから再度実行すること。
UPDATE admin_settings
SET settings = jsonb_insert(settings, '{terms_and_conditions, -1}',
    '{"key": "000000000001", "content": {"en": {"title": "TestTermTitle", "content": "TestTermContent"}, "ja": {"title": "テスト規約タイトル", "content": "テスト規約本文"}}, "existed": true}',
    true)
WHERE name = 'restricted_access';
