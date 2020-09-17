import { include } from 'named-urls'
//import ManagerURL from './ManagerURL'


export const urls = include('/publications',
    {
        stories_own: "story/",
        story_content: "story-content/:pk",
        chapter_content: "chapter-content/:pk",
        create_story: "create-story",
        create_story_cont: ":pkStory/create-story",
        create_chapter_cont: ":pkStory/:pkchapter/create-story",
        delete_story: "delete-story/:pk",
        edit_story: "edit-story/:pk",
        delete_chapter: "delete-chapter/:pk",
        edit_chapter: "edit-chapter/:pk",
        subs_story: "subscribe/:pk",
        unsubs_story: "unsubscribe/:pk",
        like_story: "story/like/:pk",
        unlike_story: "story/unlike/:pk",
        like_chapter: "chapter/like/:pk",
        unlike_chapter: "chapter/unlike/:pk",
        conts_story: "continuations/:pk",
        conts_chap: "continuations-chapter/:pk",
        conts_title_story: "continuations-titles/:pk",
        conts_title_chapter: "continuations-chapter-titles/:pk",
    });

/*
class APIPublication extends ManagerURL {

}

export default APIPublication;*/