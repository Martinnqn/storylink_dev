import { include } from 'named-urls'
//import ManagerURL from './ManagerURL'
import { urls as urlsPublication } from './URLPublication'

export const urls = include('/users/:username/',
    {
        followers: "followers/",
        following: "following/",
        follow: "follow/",
        unfollow: "unfollow/",
        edit_profile: "edit-profile/",
        delete: "delete/:id/",
        account: "edit-account/",
        search: "search/:username/",
        user_stories_subscription: "stories-subscription/",
        publication: urlsPublication,
    });



/*class ManagerUser extends ManagerURL {

}

export default ManagerUser;*/