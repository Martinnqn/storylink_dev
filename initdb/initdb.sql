--
-- PostgreSQL database dump
--

-- Dumped from database version 11.8 (Debian 11.8-1.pgdg90+1)
-- Dumped by pg_dump version 11.8 (Debian 11.8-1.pgdg90+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO nk_user;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO nk_user;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO nk_user;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO nk_user;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO nk_user;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO nk_user;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO nk_user;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO nk_user;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO nk_user;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO nk_user;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO nk_user;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO nk_user;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO nk_user;

--
-- Name: publications_chapterlike; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.publications_chapterlike (
    id integer NOT NULL,
    date_time date NOT NULL,
    from_user_id integer NOT NULL,
    to_chapter_id integer NOT NULL
);


ALTER TABLE public.publications_chapterlike OWNER TO nk_user;

--
-- Name: publications_chapterlike_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.publications_chapterlike_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publications_chapterlike_id_seq OWNER TO nk_user;

--
-- Name: publications_chapterlike_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.publications_chapterlike_id_seq OWNED BY public.publications_chapterlike.id;


--
-- Name: publications_tag; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.publications_tag (
    id integer NOT NULL,
    tag character varying(80) NOT NULL,
    creation_date_time date NOT NULL
);


ALTER TABLE public.publications_tag OWNER TO nk_user;

--
-- Name: publications_hashtag_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.publications_hashtag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publications_hashtag_id_seq OWNER TO nk_user;

--
-- Name: publications_hashtag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.publications_hashtag_id_seq OWNED BY public.publications_tag.id;


--
-- Name: publications_resourcepublication; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.publications_resourcepublication (
    id integer NOT NULL,
    user_name character varying(45) NOT NULL,
    user_lastname character varying(45) NOT NULL,
    text_content text NOT NULL,
    img_content_link character varying(500) NOT NULL,
    privacity integer NOT NULL,
    date_time date NOT NULL,
    views integer NOT NULL,
    own_user_id integer NOT NULL,
    active boolean NOT NULL,
    title character varying(500) NOT NULL,
    valoration integer NOT NULL
);


ALTER TABLE public.publications_resourcepublication OWNER TO nk_user;

--
-- Name: publications_resourcepublication_tag; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.publications_resourcepublication_tag (
    id integer NOT NULL,
    resourcepublication_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.publications_resourcepublication_tag OWNER TO nk_user;

--
-- Name: publications_resourcepublication_hashtag_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.publications_resourcepublication_hashtag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publications_resourcepublication_hashtag_id_seq OWNER TO nk_user;

--
-- Name: publications_resourcepublication_hashtag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.publications_resourcepublication_hashtag_id_seq OWNED BY public.publications_resourcepublication_tag.id;


--
-- Name: publications_resourcepublication_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.publications_resourcepublication_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publications_resourcepublication_id_seq OWNER TO nk_user;

--
-- Name: publications_resourcepublication_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.publications_resourcepublication_id_seq OWNED BY public.publications_resourcepublication.id;


--
-- Name: publications_storychapter; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.publications_storychapter (
    id integer NOT NULL,
    text_content text NOT NULL,
    active boolean NOT NULL,
    date_time date NOT NULL,
    views integer NOT NULL,
    valoration integer NOT NULL,
    quest_answ character varying(100) NOT NULL,
    "mainStory_id" integer NOT NULL,
    own_user_id integer NOT NULL,
    "prevChapter_id" integer
);


ALTER TABLE public.publications_storychapter OWNER TO nk_user;

--
-- Name: publications_storychapter_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.publications_storychapter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publications_storychapter_id_seq OWNER TO nk_user;

--
-- Name: publications_storychapter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.publications_storychapter_id_seq OWNED BY public.publications_storychapter.id;


--
-- Name: publications_storychapter_tag; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.publications_storychapter_tag (
    id integer NOT NULL,
    storychapter_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.publications_storychapter_tag OWNER TO nk_user;

--
-- Name: publications_storychapter_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.publications_storychapter_tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publications_storychapter_tag_id_seq OWNER TO nk_user;

--
-- Name: publications_storychapter_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.publications_storychapter_tag_id_seq OWNED BY public.publications_storychapter_tag.id;


--
-- Name: publications_storylike; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.publications_storylike (
    id integer NOT NULL,
    date_time date NOT NULL,
    from_user_id integer NOT NULL,
    to_story_id integer NOT NULL
);


ALTER TABLE public.publications_storylike OWNER TO nk_user;

--
-- Name: publications_storylike_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.publications_storylike_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publications_storylike_id_seq OWNER TO nk_user;

--
-- Name: publications_storylike_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.publications_storylike_id_seq OWNED BY public.publications_storylike.id;


--
-- Name: publications_storypublication; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.publications_storypublication (
    id integer NOT NULL,
    text_content text NOT NULL,
    img_content_link character varying(100) NOT NULL,
    date_time date NOT NULL,
    views integer NOT NULL,
    valoration integer NOT NULL,
    own_user_id integer NOT NULL,
    active boolean NOT NULL,
    title character varying(120) NOT NULL,
    color character varying(7) NOT NULL,
    status character varying(2) NOT NULL
);


ALTER TABLE public.publications_storypublication OWNER TO nk_user;

--
-- Name: publications_storypublication_tag; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.publications_storypublication_tag (
    id integer NOT NULL,
    storypublication_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.publications_storypublication_tag OWNER TO nk_user;

--
-- Name: publications_storypublication_hashtag_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.publications_storypublication_hashtag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publications_storypublication_hashtag_id_seq OWNER TO nk_user;

--
-- Name: publications_storypublication_hashtag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.publications_storypublication_hashtag_id_seq OWNED BY public.publications_storypublication_tag.id;


--
-- Name: publications_storypublication_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.publications_storypublication_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publications_storypublication_id_seq OWNER TO nk_user;

--
-- Name: publications_storypublication_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.publications_storypublication_id_seq OWNED BY public.publications_storypublication.id;


--
-- Name: social_auth_association; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.social_auth_association (
    id integer NOT NULL,
    server_url character varying(255) NOT NULL,
    handle character varying(255) NOT NULL,
    secret character varying(255) NOT NULL,
    issued integer NOT NULL,
    lifetime integer NOT NULL,
    assoc_type character varying(64) NOT NULL
);


ALTER TABLE public.social_auth_association OWNER TO nk_user;

--
-- Name: social_auth_association_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.social_auth_association_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.social_auth_association_id_seq OWNER TO nk_user;

--
-- Name: social_auth_association_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.social_auth_association_id_seq OWNED BY public.social_auth_association.id;


--
-- Name: social_auth_code; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.social_auth_code (
    id integer NOT NULL,
    email character varying(254) NOT NULL,
    code character varying(32) NOT NULL,
    verified boolean NOT NULL,
    "timestamp" timestamp with time zone NOT NULL
);


ALTER TABLE public.social_auth_code OWNER TO nk_user;

--
-- Name: social_auth_code_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.social_auth_code_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.social_auth_code_id_seq OWNER TO nk_user;

--
-- Name: social_auth_code_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.social_auth_code_id_seq OWNED BY public.social_auth_code.id;


--
-- Name: social_auth_nonce; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.social_auth_nonce (
    id integer NOT NULL,
    server_url character varying(255) NOT NULL,
    "timestamp" integer NOT NULL,
    salt character varying(65) NOT NULL
);


ALTER TABLE public.social_auth_nonce OWNER TO nk_user;

--
-- Name: social_auth_nonce_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.social_auth_nonce_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.social_auth_nonce_id_seq OWNER TO nk_user;

--
-- Name: social_auth_nonce_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.social_auth_nonce_id_seq OWNED BY public.social_auth_nonce.id;


--
-- Name: social_auth_partial; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.social_auth_partial (
    id integer NOT NULL,
    token character varying(32) NOT NULL,
    next_step smallint NOT NULL,
    backend character varying(32) NOT NULL,
    data jsonb NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    CONSTRAINT social_auth_partial_next_step_check CHECK ((next_step >= 0))
);


ALTER TABLE public.social_auth_partial OWNER TO nk_user;

--
-- Name: social_auth_partial_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.social_auth_partial_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.social_auth_partial_id_seq OWNER TO nk_user;

--
-- Name: social_auth_partial_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.social_auth_partial_id_seq OWNED BY public.social_auth_partial.id;


--
-- Name: social_auth_usersocialauth; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.social_auth_usersocialauth (
    id integer NOT NULL,
    provider character varying(32) NOT NULL,
    uid character varying(255) NOT NULL,
    extra_data jsonb NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.social_auth_usersocialauth OWNER TO nk_user;

--
-- Name: social_auth_usersocialauth_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.social_auth_usersocialauth_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.social_auth_usersocialauth_id_seq OWNER TO nk_user;

--
-- Name: social_auth_usersocialauth_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.social_auth_usersocialauth_id_seq OWNED BY public.social_auth_usersocialauth.id;


--
-- Name: users_customuser; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.users_customuser (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(35) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    email_verified boolean NOT NULL
);


ALTER TABLE public.users_customuser OWNER TO nk_user;

--
-- Name: users_customuser_groups; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.users_customuser_groups (
    id integer NOT NULL,
    customuser_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.users_customuser_groups OWNER TO nk_user;

--
-- Name: users_customuser_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.users_customuser_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_customuser_groups_id_seq OWNER TO nk_user;

--
-- Name: users_customuser_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.users_customuser_groups_id_seq OWNED BY public.users_customuser_groups.id;


--
-- Name: users_customuser_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.users_customuser_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_customuser_id_seq OWNER TO nk_user;

--
-- Name: users_customuser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.users_customuser_id_seq OWNED BY public.users_customuser.id;


--
-- Name: users_customuser_user_permissions; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.users_customuser_user_permissions (
    id integer NOT NULL,
    customuser_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.users_customuser_user_permissions OWNER TO nk_user;

--
-- Name: users_customuser_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.users_customuser_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_customuser_user_permissions_id_seq OWNER TO nk_user;

--
-- Name: users_customuser_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.users_customuser_user_permissions_id_seq OWNED BY public.users_customuser_user_permissions.id;


--
-- Name: users_pubsubscriptionmodelaux; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.users_pubsubscriptionmodelaux (
    id integer NOT NULL,
    date_time date NOT NULL,
    pub_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.users_pubsubscriptionmodelaux OWNER TO nk_user;

--
-- Name: users_pubsubscriptionmodelaux_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.users_pubsubscriptionmodelaux_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_pubsubscriptionmodelaux_id_seq OWNER TO nk_user;

--
-- Name: users_pubsubscriptionmodelaux_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.users_pubsubscriptionmodelaux_id_seq OWNED BY public.users_pubsubscriptionmodelaux.id;


--
-- Name: users_userevents; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.users_userevents (
    id integer NOT NULL,
    date_time date NOT NULL,
    event_type character varying(5) NOT NULL,
    id_publication integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.users_userevents OWNER TO nk_user;

--
-- Name: users_userevents_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.users_userevents_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_userevents_id_seq OWNER TO nk_user;

--
-- Name: users_userevents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.users_userevents_id_seq OWNED BY public.users_userevents.id;


--
-- Name: users_userprofile; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.users_userprofile (
    id integer NOT NULL,
    link_img_perfil character varying(350) NOT NULL,
    description character varying(150) NOT NULL,
    user_id integer NOT NULL,
    is_reported boolean NOT NULL
);


ALTER TABLE public.users_userprofile OWNER TO nk_user;

--
-- Name: users_userprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.users_userprofile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_userprofile_id_seq OWNER TO nk_user;

--
-- Name: users_userprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.users_userprofile_id_seq OWNED BY public.users_userprofile.id;


--
-- Name: users_usersubscriptionmodelaux; Type: TABLE; Schema: public; Owner: nk_user
--

CREATE TABLE public.users_usersubscriptionmodelaux (
    id integer NOT NULL,
    date_time date NOT NULL,
    from_user_id integer NOT NULL,
    to_user_id integer NOT NULL
);


ALTER TABLE public.users_usersubscriptionmodelaux OWNER TO nk_user;

--
-- Name: users_usersubscriptionmodelaux_id_seq; Type: SEQUENCE; Schema: public; Owner: nk_user
--

CREATE SEQUENCE public.users_usersubscriptionmodelaux_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_usersubscriptionmodelaux_id_seq OWNER TO nk_user;

--
-- Name: users_usersubscriptionmodelaux_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nk_user
--

ALTER SEQUENCE public.users_usersubscriptionmodelaux_id_seq OWNED BY public.users_usersubscriptionmodelaux.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: publications_chapterlike id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_chapterlike ALTER COLUMN id SET DEFAULT nextval('public.publications_chapterlike_id_seq'::regclass);


--
-- Name: publications_resourcepublication id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_resourcepublication ALTER COLUMN id SET DEFAULT nextval('public.publications_resourcepublication_id_seq'::regclass);


--
-- Name: publications_resourcepublication_tag id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_resourcepublication_tag ALTER COLUMN id SET DEFAULT nextval('public.publications_resourcepublication_hashtag_id_seq'::regclass);


--
-- Name: publications_storychapter id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storychapter ALTER COLUMN id SET DEFAULT nextval('public.publications_storychapter_id_seq'::regclass);


--
-- Name: publications_storychapter_tag id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storychapter_tag ALTER COLUMN id SET DEFAULT nextval('public.publications_storychapter_tag_id_seq'::regclass);


--
-- Name: publications_storylike id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storylike ALTER COLUMN id SET DEFAULT nextval('public.publications_storylike_id_seq'::regclass);


--
-- Name: publications_storypublication id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storypublication ALTER COLUMN id SET DEFAULT nextval('public.publications_storypublication_id_seq'::regclass);


--
-- Name: publications_storypublication_tag id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storypublication_tag ALTER COLUMN id SET DEFAULT nextval('public.publications_storypublication_hashtag_id_seq'::regclass);


--
-- Name: publications_tag id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_tag ALTER COLUMN id SET DEFAULT nextval('public.publications_hashtag_id_seq'::regclass);


--
-- Name: social_auth_association id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_association ALTER COLUMN id SET DEFAULT nextval('public.social_auth_association_id_seq'::regclass);


--
-- Name: social_auth_code id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_code ALTER COLUMN id SET DEFAULT nextval('public.social_auth_code_id_seq'::regclass);


--
-- Name: social_auth_nonce id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_nonce ALTER COLUMN id SET DEFAULT nextval('public.social_auth_nonce_id_seq'::regclass);


--
-- Name: social_auth_partial id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_partial ALTER COLUMN id SET DEFAULT nextval('public.social_auth_partial_id_seq'::regclass);


--
-- Name: social_auth_usersocialauth id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_usersocialauth ALTER COLUMN id SET DEFAULT nextval('public.social_auth_usersocialauth_id_seq'::regclass);


--
-- Name: users_customuser id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser ALTER COLUMN id SET DEFAULT nextval('public.users_customuser_id_seq'::regclass);


--
-- Name: users_customuser_groups id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser_groups ALTER COLUMN id SET DEFAULT nextval('public.users_customuser_groups_id_seq'::regclass);


--
-- Name: users_customuser_user_permissions id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.users_customuser_user_permissions_id_seq'::regclass);


--
-- Name: users_pubsubscriptionmodelaux id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_pubsubscriptionmodelaux ALTER COLUMN id SET DEFAULT nextval('public.users_pubsubscriptionmodelaux_id_seq'::regclass);


--
-- Name: users_userevents id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_userevents ALTER COLUMN id SET DEFAULT nextval('public.users_userevents_id_seq'::regclass);


--
-- Name: users_userprofile id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_userprofile ALTER COLUMN id SET DEFAULT nextval('public.users_userprofile_id_seq'::regclass);


--
-- Name: users_usersubscriptionmodelaux id; Type: DEFAULT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_usersubscriptionmodelaux ALTER COLUMN id SET DEFAULT nextval('public.users_usersubscriptionmodelaux_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add user	6	add_customuser
22	Can change user	6	change_customuser
23	Can delete user	6	delete_customuser
24	Can view user	6	view_customuser
25	Can add user subscription model aux	7	add_usersubscriptionmodelaux
26	Can change user subscription model aux	7	change_usersubscriptionmodelaux
27	Can delete user subscription model aux	7	delete_usersubscriptionmodelaux
28	Can view user subscription model aux	7	view_usersubscriptionmodelaux
29	Can add user events	8	add_userevents
30	Can change user events	8	change_userevents
31	Can delete user events	8	delete_userevents
32	Can view user events	8	view_userevents
33	Can add pub subscription model aux	9	add_pubsubscriptionmodelaux
34	Can change pub subscription model aux	9	change_pubsubscriptionmodelaux
35	Can delete pub subscription model aux	9	delete_pubsubscriptionmodelaux
36	Can view pub subscription model aux	9	view_pubsubscriptionmodelaux
37	Can add user profile	10	add_userprofile
38	Can change user profile	10	change_userprofile
39	Can delete user profile	10	delete_userprofile
40	Can view user profile	10	view_userprofile
41	Can add resource publication	11	add_resourcepublication
42	Can change resource publication	11	change_resourcepublication
43	Can delete resource publication	11	delete_resourcepublication
44	Can view resource publication	11	view_resourcepublication
45	Can add story publication	12	add_storypublication
46	Can change story publication	12	change_storypublication
47	Can delete story publication	12	delete_storypublication
48	Can view story publication	12	view_storypublication
49	Can add tag	13	add_tag
50	Can change tag	13	change_tag
51	Can delete tag	13	delete_tag
52	Can view tag	13	view_tag
53	Can add story chapter	14	add_storychapter
54	Can change story chapter	14	change_storychapter
55	Can delete story chapter	14	delete_storychapter
56	Can view story chapter	14	view_storychapter
57	Can add story like	15	add_storylike
58	Can change story like	15	change_storylike
59	Can delete story like	15	delete_storylike
60	Can view story like	15	view_storylike
61	Can add chapter like	16	add_chapterlike
62	Can change chapter like	16	change_chapterlike
63	Can delete chapter like	16	delete_chapterlike
64	Can view chapter like	16	view_chapterlike
65	Can add association	17	add_association
66	Can change association	17	change_association
67	Can delete association	17	delete_association
68	Can view association	17	view_association
69	Can add code	18	add_code
70	Can change code	18	change_code
71	Can delete code	18	delete_code
72	Can view code	18	view_code
73	Can add nonce	19	add_nonce
74	Can change nonce	19	change_nonce
75	Can delete nonce	19	delete_nonce
76	Can view nonce	19	view_nonce
77	Can add user social auth	20	add_usersocialauth
78	Can change user social auth	20	change_usersocialauth
79	Can delete user social auth	20	delete_usersocialauth
80	Can view user social auth	20	view_usersocialauth
81	Can add partial	21	add_partial
82	Can change partial	21	change_partial
83	Can delete partial	21	delete_partial
84	Can view partial	21	view_partial
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2020-08-25 13:38:45.668765+00	1	admin	2	[{"changed": {"fields": ["Email verified"]}}]	6	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	users	customuser
7	users	usersubscriptionmodelaux
8	users	userevents
9	users	pubsubscriptionmodelaux
10	users	userprofile
11	publications	resourcepublication
12	publications	storypublication
13	publications	tag
14	publications	storychapter
15	publications	storylike
16	publications	chapterlike
17	social_django	association
18	social_django	code
19	social_django	nonce
20	social_django	usersocialauth
21	social_django	partial
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	publications	0001_initial	2020-08-25 13:36:59.781331+00
2	contenttypes	0001_initial	2020-08-25 13:37:00.029952+00
3	contenttypes	0002_remove_content_type_name	2020-08-25 13:37:00.057452+00
4	auth	0001_initial	2020-08-25 13:37:00.228358+00
5	auth	0002_alter_permission_name_max_length	2020-08-25 13:37:00.4762+00
6	auth	0003_alter_user_email_max_length	2020-08-25 13:37:00.488205+00
7	auth	0004_alter_user_username_opts	2020-08-25 13:37:00.498448+00
8	auth	0005_alter_user_last_login_null	2020-08-25 13:37:00.509991+00
9	auth	0006_require_contenttypes_0002	2020-08-25 13:37:00.517438+00
10	auth	0007_alter_validators_add_error_messages	2020-08-25 13:37:00.532039+00
11	auth	0008_alter_user_username_max_length	2020-08-25 13:37:00.543498+00
12	auth	0009_alter_user_last_name_max_length	2020-08-25 13:37:00.557838+00
13	auth	0010_alter_group_name_max_length	2020-08-25 13:37:00.568727+00
14	auth	0011_update_proxy_permissions	2020-08-25 13:37:00.581876+00
15	users	0001_initial	2020-08-25 13:37:00.970593+00
16	admin	0001_initial	2020-08-25 13:37:01.630211+00
17	admin	0002_logentry_remove_auto_add	2020-08-25 13:37:01.737688+00
18	admin	0003_logentry_add_action_flag_choices	2020-08-25 13:37:01.759053+00
19	users	0002_auto_20190507_1526	2020-08-25 13:37:02.060503+00
20	users	0003_auto_20190507_1536	2020-08-25 13:37:02.100616+00
21	users	0004_auto_20190507_1546	2020-08-25 13:37:02.124317+00
22	users	0005_auto_20190917_1221	2020-08-25 13:37:02.252709+00
23	users	0006_auto_20190930_1041	2020-08-25 13:37:02.303783+00
24	users	0007_auto_20191127_1512	2020-08-25 13:37:02.364332+00
25	users	0008_auto_20191204_1226	2020-08-25 13:37:02.393498+00
26	users	0009_auto_20200328_1707	2020-08-25 13:37:02.680228+00
27	users	0010_auto_20200415_1606	2020-08-25 13:37:03.1748+00
28	users	0011_auto_20200417_0944	2020-08-25 13:37:03.214402+00
29	users	0012_auto_20200418_0936	2020-08-25 13:37:03.244157+00
30	users	0013_auto_20200418_1406	2020-08-25 13:37:03.261639+00
31	users	0014_auto_20200418_1408	2020-08-25 13:37:03.284596+00
32	users	0015_userprofile	2020-08-25 13:37:03.386748+00
33	publications	0002_auto_20190428_2052	2020-08-25 13:37:03.748491+00
34	publications	0003_auto_20191001_2029	2020-08-25 13:37:04.619779+00
35	publications	0004_auto_20191127_1536	2020-08-25 13:37:04.70894+00
36	publications	0005_resourcepublication_valoration	2020-08-25 13:37:04.733652+00
37	publications	0006_remove_storypublication_genre	2020-08-25 13:37:04.782319+00
38	publications	0007_auto_20200328_1707	2020-08-25 13:37:05.211148+00
39	publications	0008_remove_hascontinuation_quest_answ	2020-08-25 13:37:05.237554+00
40	publications	0009_auto_20200330_0925	2020-08-25 13:37:05.278147+00
41	publications	0010_storypublication_first_story	2020-08-25 13:37:05.293861+00
42	publications	0011_auto_20200402_1633	2020-08-25 13:37:05.527237+00
43	publications	0012_auto_20200415_1606	2020-08-25 13:37:05.963862+00
44	publications	0013_storypublication_color	2020-08-25 13:37:05.989047+00
45	publications	0014_auto_20200427_1500	2020-08-25 13:37:06.015398+00
46	publications	0015_auto_20200505_0924	2020-08-25 13:37:06.031245+00
47	users	0016_auto_20200505_1412	2020-08-25 13:37:06.182114+00
48	users	0017_userprofile_full_link_img_perfil	2020-08-25 13:37:06.242936+00
49	users	0018_remove_userprofile_full_link_img_perfil	2020-08-25 13:37:06.273724+00
50	users	0019_auto_20200506_1007	2020-08-25 13:37:06.293993+00
51	users	0020_customuser_email_verified	2020-08-25 13:37:06.310952+00
52	publications	0016_auto_20200506_1007	2020-08-25 13:37:06.375059+00
53	publications	0017_auto_20200508_1258	2020-08-25 13:37:06.401408+00
54	publications	0018_auto_20200510_1459	2020-08-25 13:37:06.550486+00
55	publications	0019_auto_20200524_1012	2020-08-25 13:37:06.781448+00
56	publications	0020_remove_storychapter_privated	2020-08-25 13:37:06.804571+00
57	publications	0021_storypublication_status	2020-08-25 13:37:06.826777+00
58	publications	0022_auto_20200529_1202	2020-08-25 13:37:06.866657+00
59	sessions	0001_initial	2020-08-25 13:37:06.957305+00
60	default	0001_initial	2020-08-25 13:37:07.446722+00
61	social_auth	0001_initial	2020-08-25 13:37:07.44785+00
62	default	0002_add_related_name	2020-08-25 13:37:07.625846+00
63	social_auth	0002_add_related_name	2020-08-25 13:37:07.626895+00
64	default	0003_alter_email_max_length	2020-08-25 13:37:07.643731+00
65	social_auth	0003_alter_email_max_length	2020-08-25 13:37:07.644943+00
66	default	0004_auto_20160423_0400	2020-08-25 13:37:07.65814+00
67	social_auth	0004_auto_20160423_0400	2020-08-25 13:37:07.659525+00
68	social_auth	0005_auto_20160727_2333	2020-08-25 13:37:07.717077+00
69	social_django	0006_partial	2020-08-25 13:37:07.830009+00
70	social_django	0007_code_timestamp	2020-08-25 13:37:07.952118+00
71	social_django	0008_partial_timestamp	2020-08-25 13:37:08.019931+00
72	users	0021_auto_20200524_1012	2020-08-25 13:37:08.094145+00
73	social_django	0003_alter_email_max_length	2020-08-25 13:37:08.108334+00
74	social_django	0001_initial	2020-08-25 13:37:08.117736+00
75	social_django	0002_add_related_name	2020-08-25 13:37:08.129072+00
76	social_django	0005_auto_20160727_2333	2020-08-25 13:37:08.139195+00
77	social_django	0004_auto_20160423_0400	2020-08-25 13:37:08.150373+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
01aoqm7py3myh0vl22yepkhbeswc04v3	NzVmZDA4MzQ1MTYxNDhmZTY1MjBkYzMzYjc5NWNlZDYyNmU2MDczNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5BbGxvd0FsbFVzZXJzTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMjlmYzZjMTE1MDQyYjU5ODgxYmU5NjA5OTU4MTJhNjdlZmY4OWE5OCJ9	2020-09-08 13:41:00.766041+00
\.


--
-- Data for Name: publications_chapterlike; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.publications_chapterlike (id, date_time, from_user_id, to_chapter_id) FROM stdin;
\.


--
-- Data for Name: publications_resourcepublication; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.publications_resourcepublication (id, user_name, user_lastname, text_content, img_content_link, privacity, date_time, views, own_user_id, active, title, valoration) FROM stdin;
\.


--
-- Data for Name: publications_resourcepublication_tag; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.publications_resourcepublication_tag (id, resourcepublication_id, tag_id) FROM stdin;
\.


--
-- Data for Name: publications_storychapter; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.publications_storychapter (id, text_content, active, date_time, views, valoration, quest_answ, "mainStory_id", own_user_id, "prevChapter_id") FROM stdin;
\.


--
-- Data for Name: publications_storychapter_tag; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.publications_storychapter_tag (id, storychapter_id, tag_id) FROM stdin;
\.


--
-- Data for Name: publications_storylike; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.publications_storylike (id, date_time, from_user_id, to_story_id) FROM stdin;
\.


--
-- Data for Name: publications_storypublication; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.publications_storypublication (id, text_content, img_content_link, date_time, views, valoration, own_user_id, active, title, color, status) FROM stdin;
\.


--
-- Data for Name: publications_storypublication_tag; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.publications_storypublication_tag (id, storypublication_id, tag_id) FROM stdin;
\.


--
-- Data for Name: publications_tag; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.publications_tag (id, tag, creation_date_time) FROM stdin;
\.


--
-- Data for Name: social_auth_association; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.social_auth_association (id, server_url, handle, secret, issued, lifetime, assoc_type) FROM stdin;
\.


--
-- Data for Name: social_auth_code; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.social_auth_code (id, email, code, verified, "timestamp") FROM stdin;
\.


--
-- Data for Name: social_auth_nonce; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.social_auth_nonce (id, server_url, "timestamp", salt) FROM stdin;
\.


--
-- Data for Name: social_auth_partial; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.social_auth_partial (id, token, next_step, backend, data, "timestamp") FROM stdin;
\.


--
-- Data for Name: social_auth_usersocialauth; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.social_auth_usersocialauth (id, provider, uid, extra_data, user_id) FROM stdin;
\.


--
-- Data for Name: users_customuser; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.users_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, date_joined, is_active, email_verified) FROM stdin;
1	pbkdf2_sha256$180000$aaaOzdfODDXf$DlRqQdflwyzdUG0f+3a4HCQSHYWZo4xWxe/qgMiHeoI=	2020-08-25 13:41:00.754516+00	t	admin			admin@admin.com	t	2020-08-25 13:37:42+00	t	t
\.


--
-- Data for Name: users_customuser_groups; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.users_customuser_groups (id, customuser_id, group_id) FROM stdin;
\.


--
-- Data for Name: users_customuser_user_permissions; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.users_customuser_user_permissions (id, customuser_id, permission_id) FROM stdin;
\.


--
-- Data for Name: users_pubsubscriptionmodelaux; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.users_pubsubscriptionmodelaux (id, date_time, pub_id, user_id) FROM stdin;
\.


--
-- Data for Name: users_userevents; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.users_userevents (id, date_time, event_type, id_publication, user_id) FROM stdin;
\.


--
-- Data for Name: users_userprofile; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.users_userprofile (id, link_img_perfil, description, user_id, is_reported) FROM stdin;
1	users/user_1/img1.png	soy un admin	1	f
\.


--
-- Data for Name: users_usersubscriptionmodelaux; Type: TABLE DATA; Schema: public; Owner: nk_user
--

COPY public.users_usersubscriptionmodelaux (id, date_time, from_user_id, to_user_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 84, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 21, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 77, true);


--
-- Name: publications_chapterlike_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.publications_chapterlike_id_seq', 1, false);


--
-- Name: publications_hashtag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.publications_hashtag_id_seq', 1, false);


--
-- Name: publications_resourcepublication_hashtag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.publications_resourcepublication_hashtag_id_seq', 1, false);


--
-- Name: publications_resourcepublication_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.publications_resourcepublication_id_seq', 1, false);


--
-- Name: publications_storychapter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.publications_storychapter_id_seq', 1, false);


--
-- Name: publications_storychapter_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.publications_storychapter_tag_id_seq', 1, false);


--
-- Name: publications_storylike_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.publications_storylike_id_seq', 1, false);


--
-- Name: publications_storypublication_hashtag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.publications_storypublication_hashtag_id_seq', 1, false);


--
-- Name: publications_storypublication_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.publications_storypublication_id_seq', 1, false);


--
-- Name: social_auth_association_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.social_auth_association_id_seq', 1, false);


--
-- Name: social_auth_code_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.social_auth_code_id_seq', 1, false);


--
-- Name: social_auth_nonce_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.social_auth_nonce_id_seq', 1, false);


--
-- Name: social_auth_partial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.social_auth_partial_id_seq', 1, false);


--
-- Name: social_auth_usersocialauth_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.social_auth_usersocialauth_id_seq', 1, false);


--
-- Name: users_customuser_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.users_customuser_groups_id_seq', 1, false);


--
-- Name: users_customuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.users_customuser_id_seq', 1, true);


--
-- Name: users_customuser_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.users_customuser_user_permissions_id_seq', 1, false);


--
-- Name: users_pubsubscriptionmodelaux_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.users_pubsubscriptionmodelaux_id_seq', 1, false);


--
-- Name: users_userevents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.users_userevents_id_seq', 1, false);


--
-- Name: users_userprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.users_userprofile_id_seq', 1, true);


--
-- Name: users_usersubscriptionmodelaux_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nk_user
--

SELECT pg_catalog.setval('public.users_usersubscriptionmodelaux_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: publications_chapterlike publications_chapterlike_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_chapterlike
    ADD CONSTRAINT publications_chapterlike_pkey PRIMARY KEY (id);


--
-- Name: publications_tag publications_hashtag_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_tag
    ADD CONSTRAINT publications_hashtag_pkey PRIMARY KEY (id);


--
-- Name: publications_resourcepublication_tag publications_resourcepub_resourcepublication_id_h_887ad9c0_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_resourcepublication_tag
    ADD CONSTRAINT publications_resourcepub_resourcepublication_id_h_887ad9c0_uniq UNIQUE (resourcepublication_id, tag_id);


--
-- Name: publications_resourcepublication_tag publications_resourcepublication_hashtag_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_resourcepublication_tag
    ADD CONSTRAINT publications_resourcepublication_hashtag_pkey PRIMARY KEY (id);


--
-- Name: publications_resourcepublication publications_resourcepublication_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_resourcepublication
    ADD CONSTRAINT publications_resourcepublication_pkey PRIMARY KEY (id);


--
-- Name: publications_storychapter_tag publications_storychapte_storychapter_id_tag_id_b71a7321_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storychapter_tag
    ADD CONSTRAINT publications_storychapte_storychapter_id_tag_id_b71a7321_uniq UNIQUE (storychapter_id, tag_id);


--
-- Name: publications_storychapter publications_storychapter_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storychapter
    ADD CONSTRAINT publications_storychapter_pkey PRIMARY KEY (id);


--
-- Name: publications_storychapter_tag publications_storychapter_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storychapter_tag
    ADD CONSTRAINT publications_storychapter_tag_pkey PRIMARY KEY (id);


--
-- Name: publications_storylike publications_storylike_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storylike
    ADD CONSTRAINT publications_storylike_pkey PRIMARY KEY (id);


--
-- Name: publications_storypublication_tag publications_storypublic_storypublication_id_hash_218f00d6_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storypublication_tag
    ADD CONSTRAINT publications_storypublic_storypublication_id_hash_218f00d6_uniq UNIQUE (storypublication_id, tag_id);


--
-- Name: publications_storypublication_tag publications_storypublication_hashtag_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storypublication_tag
    ADD CONSTRAINT publications_storypublication_hashtag_pkey PRIMARY KEY (id);


--
-- Name: publications_storypublication publications_storypublication_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storypublication
    ADD CONSTRAINT publications_storypublication_pkey PRIMARY KEY (id);


--
-- Name: social_auth_association social_auth_association_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_association
    ADD CONSTRAINT social_auth_association_pkey PRIMARY KEY (id);


--
-- Name: social_auth_association social_auth_association_server_url_handle_078befa2_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_association
    ADD CONSTRAINT social_auth_association_server_url_handle_078befa2_uniq UNIQUE (server_url, handle);


--
-- Name: social_auth_code social_auth_code_email_code_801b2d02_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_code
    ADD CONSTRAINT social_auth_code_email_code_801b2d02_uniq UNIQUE (email, code);


--
-- Name: social_auth_code social_auth_code_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_code
    ADD CONSTRAINT social_auth_code_pkey PRIMARY KEY (id);


--
-- Name: social_auth_nonce social_auth_nonce_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_nonce
    ADD CONSTRAINT social_auth_nonce_pkey PRIMARY KEY (id);


--
-- Name: social_auth_nonce social_auth_nonce_server_url_timestamp_salt_f6284463_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_nonce
    ADD CONSTRAINT social_auth_nonce_server_url_timestamp_salt_f6284463_uniq UNIQUE (server_url, "timestamp", salt);


--
-- Name: social_auth_partial social_auth_partial_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_partial
    ADD CONSTRAINT social_auth_partial_pkey PRIMARY KEY (id);


--
-- Name: social_auth_usersocialauth social_auth_usersocialauth_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_usersocialauth
    ADD CONSTRAINT social_auth_usersocialauth_pkey PRIMARY KEY (id);


--
-- Name: social_auth_usersocialauth social_auth_usersocialauth_provider_uid_e6b5e668_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_usersocialauth
    ADD CONSTRAINT social_auth_usersocialauth_provider_uid_e6b5e668_uniq UNIQUE (provider, uid);


--
-- Name: users_customuser users_customuser_email_6445acef_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser
    ADD CONSTRAINT users_customuser_email_6445acef_uniq UNIQUE (email);


--
-- Name: users_customuser_groups users_customuser_groups_customuser_id_group_id_76b619e3_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser_groups
    ADD CONSTRAINT users_customuser_groups_customuser_id_group_id_76b619e3_uniq UNIQUE (customuser_id, group_id);


--
-- Name: users_customuser_groups users_customuser_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser_groups
    ADD CONSTRAINT users_customuser_groups_pkey PRIMARY KEY (id);


--
-- Name: users_customuser users_customuser_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser
    ADD CONSTRAINT users_customuser_pkey PRIMARY KEY (id);


--
-- Name: users_customuser_user_permissions users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser_user_permissions
    ADD CONSTRAINT users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq UNIQUE (customuser_id, permission_id);


--
-- Name: users_customuser_user_permissions users_customuser_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser_user_permissions
    ADD CONSTRAINT users_customuser_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: users_customuser users_customuser_username_80452fdf_uniq; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser
    ADD CONSTRAINT users_customuser_username_80452fdf_uniq UNIQUE (username);


--
-- Name: users_pubsubscriptionmodelaux users_pubsubscriptionmodelaux_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_pubsubscriptionmodelaux
    ADD CONSTRAINT users_pubsubscriptionmodelaux_pkey PRIMARY KEY (id);


--
-- Name: users_userevents users_userevents_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_userevents
    ADD CONSTRAINT users_userevents_pkey PRIMARY KEY (id);


--
-- Name: users_userprofile users_userprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_userprofile
    ADD CONSTRAINT users_userprofile_pkey PRIMARY KEY (id);


--
-- Name: users_usersubscriptionmodelaux users_usersubscriptionmodelaux_pkey; Type: CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_usersubscriptionmodelaux
    ADD CONSTRAINT users_usersubscriptionmodelaux_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: publications_chapterlike_from_user_id_626e3c46; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_chapterlike_from_user_id_626e3c46 ON public.publications_chapterlike USING btree (from_user_id);


--
-- Name: publications_chapterlike_to_chapter_id_ffa9c1a1; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_chapterlike_to_chapter_id_ffa9c1a1 ON public.publications_chapterlike USING btree (to_chapter_id);


--
-- Name: publications_resourcepubli_resourcepublication_id_5b8d146f; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_resourcepubli_resourcepublication_id_5b8d146f ON public.publications_resourcepublication_tag USING btree (resourcepublication_id);


--
-- Name: publications_resourcepublication_hashtag_hashtag_id_e48fc2e4; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_resourcepublication_hashtag_hashtag_id_e48fc2e4 ON public.publications_resourcepublication_tag USING btree (tag_id);


--
-- Name: publications_resourcepublication_own_user_id_b021e1fa; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_resourcepublication_own_user_id_b021e1fa ON public.publications_resourcepublication USING btree (own_user_id);


--
-- Name: publications_storychapter_mainStory_id_dff5c2cf; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX "publications_storychapter_mainStory_id_dff5c2cf" ON public.publications_storychapter USING btree ("mainStory_id");


--
-- Name: publications_storychapter_own_user_id_43d2c36a; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_storychapter_own_user_id_43d2c36a ON public.publications_storychapter USING btree (own_user_id);


--
-- Name: publications_storychapter_prevChapter_id_3c06bb1a; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX "publications_storychapter_prevChapter_id_3c06bb1a" ON public.publications_storychapter USING btree ("prevChapter_id");


--
-- Name: publications_storychapter_tag_storychapter_id_f538db1c; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_storychapter_tag_storychapter_id_f538db1c ON public.publications_storychapter_tag USING btree (storychapter_id);


--
-- Name: publications_storychapter_tag_tag_id_8a5e1ac1; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_storychapter_tag_tag_id_8a5e1ac1 ON public.publications_storychapter_tag USING btree (tag_id);


--
-- Name: publications_storylike_from_user_id_6ade40d9; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_storylike_from_user_id_6ade40d9 ON public.publications_storylike USING btree (from_user_id);


--
-- Name: publications_storylike_to_story_id_210c53d0; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_storylike_to_story_id_210c53d0 ON public.publications_storylike USING btree (to_story_id);


--
-- Name: publications_storypublicat_storypublication_id_57f86dc5; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_storypublicat_storypublication_id_57f86dc5 ON public.publications_storypublication_tag USING btree (storypublication_id);


--
-- Name: publications_storypublication_hashtag_hashtag_id_4ffa43c3; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_storypublication_hashtag_hashtag_id_4ffa43c3 ON public.publications_storypublication_tag USING btree (tag_id);


--
-- Name: publications_storypublication_own_user_id_c8becd1e; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX publications_storypublication_own_user_id_c8becd1e ON public.publications_storypublication USING btree (own_user_id);


--
-- Name: social_auth_code_code_a2393167; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX social_auth_code_code_a2393167 ON public.social_auth_code USING btree (code);


--
-- Name: social_auth_code_code_a2393167_like; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX social_auth_code_code_a2393167_like ON public.social_auth_code USING btree (code varchar_pattern_ops);


--
-- Name: social_auth_code_timestamp_176b341f; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX social_auth_code_timestamp_176b341f ON public.social_auth_code USING btree ("timestamp");


--
-- Name: social_auth_partial_timestamp_50f2119f; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX social_auth_partial_timestamp_50f2119f ON public.social_auth_partial USING btree ("timestamp");


--
-- Name: social_auth_partial_token_3017fea3; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX social_auth_partial_token_3017fea3 ON public.social_auth_partial USING btree (token);


--
-- Name: social_auth_partial_token_3017fea3_like; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX social_auth_partial_token_3017fea3_like ON public.social_auth_partial USING btree (token varchar_pattern_ops);


--
-- Name: social_auth_usersocialauth_user_id_17d28448; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX social_auth_usersocialauth_user_id_17d28448 ON public.social_auth_usersocialauth USING btree (user_id);


--
-- Name: users_customuser_email_6445acef_like; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_customuser_email_6445acef_like ON public.users_customuser USING btree (email varchar_pattern_ops);


--
-- Name: users_customuser_groups_customuser_id_958147bf; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_customuser_groups_customuser_id_958147bf ON public.users_customuser_groups USING btree (customuser_id);


--
-- Name: users_customuser_groups_group_id_01390b14; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_customuser_groups_group_id_01390b14 ON public.users_customuser_groups USING btree (group_id);


--
-- Name: users_customuser_user_permissions_customuser_id_5771478b; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_customuser_user_permissions_customuser_id_5771478b ON public.users_customuser_user_permissions USING btree (customuser_id);


--
-- Name: users_customuser_user_permissions_permission_id_baaa2f74; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_customuser_user_permissions_permission_id_baaa2f74 ON public.users_customuser_user_permissions USING btree (permission_id);


--
-- Name: users_customuser_username_80452fdf_like; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_customuser_username_80452fdf_like ON public.users_customuser USING btree (username varchar_pattern_ops);


--
-- Name: users_pubsubscriptionmodelaux_pub_id_0753a7ea; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_pubsubscriptionmodelaux_pub_id_0753a7ea ON public.users_pubsubscriptionmodelaux USING btree (pub_id);


--
-- Name: users_pubsubscriptionmodelaux_user_id_0e50d258; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_pubsubscriptionmodelaux_user_id_0e50d258 ON public.users_pubsubscriptionmodelaux USING btree (user_id);


--
-- Name: users_userevents_user_id_68c743e8; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_userevents_user_id_68c743e8 ON public.users_userevents USING btree (user_id);


--
-- Name: users_userprofile_user_id_87251ef1; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_userprofile_user_id_87251ef1 ON public.users_userprofile USING btree (user_id);


--
-- Name: users_usersubscriptionmodelaux_from_user_id_ac3ca50b; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_usersubscriptionmodelaux_from_user_id_ac3ca50b ON public.users_usersubscriptionmodelaux USING btree (from_user_id);


--
-- Name: users_usersubscriptionmodelaux_to_user_id_c647492b; Type: INDEX; Schema: public; Owner: nk_user
--

CREATE INDEX users_usersubscriptionmodelaux_to_user_id_c647492b ON public.users_usersubscriptionmodelaux USING btree (to_user_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_users_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_users_customuser_id FOREIGN KEY (user_id) REFERENCES public.users_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_chapterlike publications_chapter_from_user_id_626e3c46_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_chapterlike
    ADD CONSTRAINT publications_chapter_from_user_id_626e3c46_fk_users_use FOREIGN KEY (from_user_id) REFERENCES public.users_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_chapterlike publications_chapter_to_chapter_id_ffa9c1a1_fk_publicati; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_chapterlike
    ADD CONSTRAINT publications_chapter_to_chapter_id_ffa9c1a1_fk_publicati FOREIGN KEY (to_chapter_id) REFERENCES public.publications_storychapter(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_resourcepublication publications_resourc_own_user_id_b021e1fa_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_resourcepublication
    ADD CONSTRAINT publications_resourc_own_user_id_b021e1fa_fk_users_use FOREIGN KEY (own_user_id) REFERENCES public.users_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_resourcepublication_tag publications_resourc_resourcepublication__a6cb510d_fk_publicati; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_resourcepublication_tag
    ADD CONSTRAINT publications_resourc_resourcepublication__a6cb510d_fk_publicati FOREIGN KEY (resourcepublication_id) REFERENCES public.publications_resourcepublication(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_resourcepublication_tag publications_resourc_tag_id_3460d842_fk_publicati; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_resourcepublication_tag
    ADD CONSTRAINT publications_resourc_tag_id_3460d842_fk_publicati FOREIGN KEY (tag_id) REFERENCES public.publications_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_storychapter publications_storych_mainStory_id_dff5c2cf_fk_publicati; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storychapter
    ADD CONSTRAINT "publications_storych_mainStory_id_dff5c2cf_fk_publicati" FOREIGN KEY ("mainStory_id") REFERENCES public.publications_storypublication(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_storychapter publications_storych_own_user_id_43d2c36a_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storychapter
    ADD CONSTRAINT publications_storych_own_user_id_43d2c36a_fk_users_use FOREIGN KEY (own_user_id) REFERENCES public.users_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_storychapter publications_storych_prevChapter_id_3c06bb1a_fk_publicati; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storychapter
    ADD CONSTRAINT "publications_storych_prevChapter_id_3c06bb1a_fk_publicati" FOREIGN KEY ("prevChapter_id") REFERENCES public.publications_storychapter(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_storychapter_tag publications_storych_storychapter_id_f538db1c_fk_publicati; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storychapter_tag
    ADD CONSTRAINT publications_storych_storychapter_id_f538db1c_fk_publicati FOREIGN KEY (storychapter_id) REFERENCES public.publications_storychapter(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_storychapter_tag publications_storych_tag_id_8a5e1ac1_fk_publicati; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storychapter_tag
    ADD CONSTRAINT publications_storych_tag_id_8a5e1ac1_fk_publicati FOREIGN KEY (tag_id) REFERENCES public.publications_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_storylike publications_storyli_from_user_id_6ade40d9_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storylike
    ADD CONSTRAINT publications_storyli_from_user_id_6ade40d9_fk_users_use FOREIGN KEY (from_user_id) REFERENCES public.users_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_storylike publications_storyli_to_story_id_210c53d0_fk_publicati; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storylike
    ADD CONSTRAINT publications_storyli_to_story_id_210c53d0_fk_publicati FOREIGN KEY (to_story_id) REFERENCES public.publications_storypublication(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_storypublication publications_storypu_own_user_id_c8becd1e_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storypublication
    ADD CONSTRAINT publications_storypu_own_user_id_c8becd1e_fk_users_use FOREIGN KEY (own_user_id) REFERENCES public.users_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_storypublication_tag publications_storypu_storypublication_id_4a606f97_fk_publicati; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storypublication_tag
    ADD CONSTRAINT publications_storypu_storypublication_id_4a606f97_fk_publicati FOREIGN KEY (storypublication_id) REFERENCES public.publications_storypublication(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: publications_storypublication_tag publications_storypu_tag_id_3c4fa064_fk_publicati; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.publications_storypublication_tag
    ADD CONSTRAINT publications_storypu_tag_id_3c4fa064_fk_publicati FOREIGN KEY (tag_id) REFERENCES public.publications_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: social_auth_usersocialauth social_auth_usersoci_user_id_17d28448_fk_users_cus; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.social_auth_usersocialauth
    ADD CONSTRAINT social_auth_usersoci_user_id_17d28448_fk_users_cus FOREIGN KEY (user_id) REFERENCES public.users_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_customuser_groups users_customuser_gro_customuser_id_958147bf_fk_users_cus; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser_groups
    ADD CONSTRAINT users_customuser_gro_customuser_id_958147bf_fk_users_cus FOREIGN KEY (customuser_id) REFERENCES public.users_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_customuser_groups users_customuser_groups_group_id_01390b14_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser_groups
    ADD CONSTRAINT users_customuser_groups_group_id_01390b14_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_customuser_user_permissions users_customuser_use_customuser_id_5771478b_fk_users_cus; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser_user_permissions
    ADD CONSTRAINT users_customuser_use_customuser_id_5771478b_fk_users_cus FOREIGN KEY (customuser_id) REFERENCES public.users_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_customuser_user_permissions users_customuser_use_permission_id_baaa2f74_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_customuser_user_permissions
    ADD CONSTRAINT users_customuser_use_permission_id_baaa2f74_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_pubsubscriptionmodelaux users_pubsubscriptio_pub_id_0753a7ea_fk_publicati; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_pubsubscriptionmodelaux
    ADD CONSTRAINT users_pubsubscriptio_pub_id_0753a7ea_fk_publicati FOREIGN KEY (pub_id) REFERENCES public.publications_storypublication(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_pubsubscriptionmodelaux users_pubsubscriptio_user_id_0e50d258_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_pubsubscriptionmodelaux
    ADD CONSTRAINT users_pubsubscriptio_user_id_0e50d258_fk_users_use FOREIGN KEY (user_id) REFERENCES public.users_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_userevents users_userevents_user_id_68c743e8_fk_users_userprofile_id; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_userevents
    ADD CONSTRAINT users_userevents_user_id_68c743e8_fk_users_userprofile_id FOREIGN KEY (user_id) REFERENCES public.users_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_userprofile users_userprofile_user_id_87251ef1_fk_users_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_userprofile
    ADD CONSTRAINT users_userprofile_user_id_87251ef1_fk_users_customuser_id FOREIGN KEY (user_id) REFERENCES public.users_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_usersubscriptionmodelaux users_usersubscripti_from_user_id_ac3ca50b_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_usersubscriptionmodelaux
    ADD CONSTRAINT users_usersubscripti_from_user_id_ac3ca50b_fk_users_use FOREIGN KEY (from_user_id) REFERENCES public.users_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_usersubscriptionmodelaux users_usersubscripti_to_user_id_c647492b_fk_users_use; Type: FK CONSTRAINT; Schema: public; Owner: nk_user
--

ALTER TABLE ONLY public.users_usersubscriptionmodelaux
    ADD CONSTRAINT users_usersubscripti_to_user_id_c647492b_fk_users_use FOREIGN KEY (to_user_id) REFERENCES public.users_userprofile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

