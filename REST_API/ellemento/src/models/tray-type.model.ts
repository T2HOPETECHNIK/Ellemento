import {Entity, model, property, hasMany} from '@loopback/repository';
import {Stage} from './stage.model';

@model({settings: {strict: false}})
export class TrayType extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  tray_type_id?: number;

  @property({
    type: 'number',
  })
  size?: number;

  @property({
    type: 'number',
  })
  capacity?: number;

  @property({
    type: 'string',
  })
  description?: string;

  @hasMany(() => Stage)
  stages: Stage[];
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<TrayType>) {
    super(data);
  }
}

export interface TrayTypeRelations {
  // describe navigational properties here
}

export type TrayTypeWithRelations = TrayType & TrayTypeRelations;
