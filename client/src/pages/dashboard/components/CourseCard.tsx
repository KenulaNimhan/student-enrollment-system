import styles from "./CourseCard.module.css";

type Props = {
  subject: string;
  tutor: string;
  btnName: string;
  btnFn: () => void;
};

export const CourseCard = ({ subject, tutor, btnName, btnFn }: Props) => {
  return (
    <div className={styles.cardContainer}>
      <div className={styles.upperSection}>
        <h2>{subject}</h2>
        <h4>{tutor}</h4>
      </div>
      <button onClick={() => btnFn()}>{btnName}</button>
    </div>
  );
};
