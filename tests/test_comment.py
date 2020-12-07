from app.models import Comments,User
from app import db
def setUp(self):
        self.user_moringa = User(username = 'moringa',password = 'Access', email = 'vugutsamercy84@gmail.com')
        self.new_comment = Comment(pitch_id=12345,pitch_title='Comment for pitches',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",pitch_Comment='This pitch is the best thing since sliced bread',user = self.user_moringa )
def tearDown(self):
        Comment.query.delete()
        User.query.delete()
def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id,12345)
        self.assertEquals(self.new_comment.pitch_title,'Comment for pitches')
        self.assertEquals(self.new_comment.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_comment.pitch_Comment,'This pitch is the best ever')
        self.assertEquals(self.new_comment.user,self.user_moringa)
def test_save_Comment(self):
        self.new_comment.save_Comment()
        self.assertTrue(len(Comment.query.all())>0)
def test_get_Comment_by_id(self):
        self.new_comment.save_Comment()
        got_Comments = Comment.get_Comments(12345)
        self.assertTrue(len(got_Comments) == 1)